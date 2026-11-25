// Entry for make.fun bounty "Sum up 25 November's world news in one image"
// (news-image-20261125). Node 22, standard library only.
//
// The image is entry.png beside this file, drawn by gen_image.py (PIL +
// DejaVu Sans, run once while building the entry). This program copies it
// to /output/entry.png, byte for byte, so two runs write identical bytes.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

// Make sure the output directory exists (the grader normally provides it,
// but a missing directory must never fail the copy).
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
copyFileSync(new URL('./entry.png', import.meta.url), join(outDir, 'entry.png'));
