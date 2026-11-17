#!/usr/bin/env python3
"""QA de áudio OBRIGATÓRIO antes de qualquer upload social (regra do Xavier, 02/11/2026).

Trava criada depois do erro dos reels do bônus: 6 reels subiram com a narração
do boletim FORTE misturada por baixo da voz real, porque um arquivo de trabalho
compartilhado (public/audio.mp3, que era NARRAÇÃO) foi usado como "trilha".

O gate confere no arquivo FINAL:
  1. Existe faixa de áudio e há som audível no começo, meio e fim.
  2. IDENTIDADE (--expect): o áudio do arquivo final É o áudio esperado
     (correlação de pico >= 0.90 com a fonte/narração aprovada).
  3. CONTAMINAÇÃO (--block): NENHUM áudio da lista de bloqueio (narrações e
     áudios de OUTRAS produções recentes) pode aparecer misturado
     (correlação de pico >= 0.05 = REPROVADO).

Uso:
  qa_audio_gate.py FINAL.mp4 --expect FONTE.mp4 [--block A.mp3 B.mp4 ...]
  qa_audio_gate.py FINAL.mp4 --block PASTA_DE_NARRACOES/

Saída: PASS/FAIL por checagem; exit 0 = aprovado, 1 = reprovado.
Nunca subir vídeo sem este gate passar.
"""
import argparse, os, subprocess, sys
import numpy as np

SR = 8000
MAX_SECONDS = 90


def extract_audio(path):
    """Decodifica o áudio para float32 mono na taxa SR (None se não houver áudio)."""
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-vn", "-ac", "1",
           "-ar", str(SR), "-t", str(MAX_SECONDS), "-f", "s16le", "-"]
    out = subprocess.run(cmd, capture_output=True).stdout
    if len(out) < SR:  # menos de 1s de áudio
        return None
    return np.frombuffer(out, dtype=np.int16).astype(np.float32) / 32768.0


def rms(x):
    return float(np.sqrt(np.mean(x ** 2))) if len(x) else 0.0


def audible_thirds(x):
    """RMS do começo, meio e fim — todos precisam ter som."""
    n = len(x)
    seg = max(n // 10, SR)
    parts = [x[:seg], x[n // 2 - seg // 2: n // 2 + seg // 2], x[-seg:]]
    return [rms(p) for p in parts]


def peak_corr(a, b):
    """Maior correlação normalizada entre a e b (procura o trecho de b dentro de a e vice-versa)."""
    if a is None or b is None or len(a) == 0 or len(b) == 0:
        return 0.0
    long_, short = (a, b) if len(a) >= len(b) else (b, a)
    short = short - short.mean()
    norm = np.sqrt(np.sum(short ** 2))
    if norm == 0:
        return 0.0
    # correlação cruzada via FFT
    n = 1 << int(np.ceil(np.log2(len(long_) + len(short))))
    L = np.fft.rfft(long_ - long_.mean(), n)
    S = np.fft.rfft(short[::-1], n)
    corr = np.fft.irfft(L * S, n)
    # energia local de long_ nas janelas do tamanho de short
    csum = np.concatenate([[0.0], np.cumsum((long_ - long_.mean()) ** 2)])
    win = csum[len(short):] - csum[:-len(short)]
    denom = np.sqrt(win) * norm
    vals = corr[len(short) - 1: len(short) - 1 + len(win)]
    ok = denom > 1e-9
    if not ok.any():
        return 0.0
    return float(np.max(np.abs(vals[ok] / denom[ok])))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("final")
    ap.add_argument("--expect", help="áudio que o arquivo final DEVE conter")
    ap.add_argument("--block", nargs="*", default=[],
                    help="arquivos ou pastas que NÃO podem aparecer no áudio final")
    args = ap.parse_args()

    failures = []
    audio = extract_audio(args.final)
    if audio is None:
        print(f"FAIL  sem faixa de áudio audível: {args.final}")
        return 1
    thirds = audible_thirds(audio)
    if min(thirds) < 0.003:
        failures.append(f"trecho mudo (RMS começo/meio/fim = "
                        f"{thirds[0]:.4f}/{thirds[1]:.4f}/{thirds[2]:.4f})")
    else:
        print(f"OK    som no começo/meio/fim (RMS {thirds[0]:.3f}/{thirds[1]:.3f}/{thirds[2]:.3f})")

    if args.expect:
        exp = extract_audio(args.expect)
        c = peak_corr(audio, exp)
        if c >= 0.90:
            print(f"OK    identidade: correlação {c:.3f} com o áudio esperado")
        else:
            failures.append(f"identidade: correlação {c:.3f} < 0.90 com {args.expect}")

    block_files = []
    for b in args.block:
        if os.path.isdir(b):
            block_files += [os.path.join(b, f) for f in sorted(os.listdir(b))
                            if f.lower().endswith((".mp3", ".mp4", ".wav", ".m4a"))]
        else:
            block_files.append(b)
    for bf in block_files:
        if os.path.abspath(bf) == os.path.abspath(args.final):
            continue
        ba = extract_audio(bf)
        c = peak_corr(audio, ba)
        if c >= 0.05:
            failures.append(f"CONTAMINAÇÃO: correlação {c:.3f} com {bf}")
        else:
            print(f"OK    limpo de {os.path.basename(bf)} (correlação {c:.3f})")

    if failures:
        for f in failures:
            print("FAIL ", f)
        print("RESULTADO: REPROVADO — não subir este arquivo.")
        return 1
    print("RESULTADO: APROVADO no gate de áudio.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
