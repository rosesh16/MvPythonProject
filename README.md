# Hand-Drawn Diagram to Machine-Drawn Diagram Converter

## Overview
This project converts a hand-drawn diagram image into a clean, structured, machine-drawn digital diagram.

Input examples:
- Flowcharts
- Block diagrams
- Sketch-style process diagrams

Output targets:
- JSON graph representation
- Mermaid
- Graphviz/DOT
- SVG

The system is designed to handle noisy, imperfect hand-drawn inputs while preserving structure and meaning.

## End-to-End Pipeline
1. Image preprocessing
- Denoise and normalize scanned/captured images.
- Convert to grayscale and apply thresholding.
- Detect edges and contours to isolate diagram primitives.

2. Shape detection and classification
- Detect geometric elements such as:
  - Rectangle
  - Circle
  - Diamond
  - Arrow/connectors
- Filter noise and small irrelevant contours.

3. Text extraction (OCR)
- Extract text inside or near detected shapes.
- Clean OCR output with basic post-processing (spacing, casing, symbol cleanup).
- Map text labels to nearest valid shape region.

4. Relationship and connection analysis
- Detect connectors/arrows between shapes.
- Infer direction (source -> target) where possible.
- Build a graph representation with:
  - Nodes (shape + text + geometry)
  - Edges (connections + direction + confidence)

5. Diagram regeneration
- Produce a clean machine-drawn layout from the graph.
- Export to one or more formats: SVG, JSON, Mermaid, Graphviz.

## Core Design Goals
- Robustness to hand-drawn noise, uneven lines, and lighting variation.
- Accurate shape classification and text extraction.
- Correct mapping of connectors between shapes.
- Visually clear, professional output diagrams.
- Modular architecture for replacing/improving each stage independently.

## Proposed Project Structure
Current:
- `src/preprocess.py`: image preprocessing and edge extraction
- `src/shape_detection.py`: contour-based shape detection
- `src/main.py`: batch processing entry point

Planned extensions:
- `src/ocr.py`: OCR extraction + cleanup
- `src/connection_detection.py`: arrow/line tracing and endpoint linking
- `src/graph_builder.py`: node/edge assembly and confidence scoring
- `src/exporters/`: JSON, Mermaid, DOT, SVG exporters
- `src/layout.py`: clean diagram layout generation

## Graph Data Model (Target)
```json
{
  "nodes": [
    {
      "id": "n1",
      "shape": "rectangle",
      "text": "Start",
      "bbox": [x, y, w, h]
    }
  ],
  "edges": [
    {
      "source": "n1",
      "target": "n2",
      "type": "arrow",
      "confidence": 0.93
    }
  ]
}
```

## Near-Term Implementation Plan
1. Improve shape detector to include diamonds and arrow candidates.
2. Integrate OCR for shape labels.
3. Implement connector-to-shape mapping.
4. Build graph constructor and JSON export.
5. Add Mermaid/Graphviz export and SVG rendering.
6. Add evaluation set with noisy hand-drawn samples.

## Tech Stack
- Python
- OpenCV (`opencv-python`)
- NumPy
- OCR engine (planned: Tesseract / EasyOCR)
- Graph export/render tools (planned: Mermaid / Graphviz / SVG generator)
