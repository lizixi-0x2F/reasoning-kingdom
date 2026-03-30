import { defineUserConfig } from 'vitepress-export-pdf'

const routeOrder = [
  '/preface.html',
  '/chapter1/index.html',
  '/chapter2/index.html',
  '/chapter3/index.html',
  '/chapter4/index.html',
  '/chapter5/index.html',
  '/chapter6/index.html',
  '/chapter7/index.html',
  '/chapter8/index.html',
  '/chapter9/index.html',
  '/chapter10/index.html',
  '/chapter11/index.html',
  '/chapter12/index.html',
  '/chapter13/index.html',
]

export default defineUserConfig({
  outFile: '推理王国.pdf',
  outDir: '../',
  pdfOutlines: true,
  routePatterns: ['/**', '!/'],
  sorter: (a, b) => {
    const ai = routeOrder.indexOf(a.path)
    const bi = routeOrder.indexOf(b.path)
    if (ai === -1 && bi === -1) return 0
    if (ai === -1) return 1
    if (bi === -1) return -1
    return ai - bi
  },
  pdfOptions: {
    format: 'A4',
    printBackground: true,
    margin: { top: '60px', bottom: '60px', left: '60px', right: '60px' },
  },
})
