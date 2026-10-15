# Evaluator

Candidate product patch precedes exact protected upstream test patch, then official setup.py force-build refreshes /testbed/build/local. All native compiler output is buffered in /tmp and copied verbatim to the raw build log, preserving failure exit code. Tests load that rebuilt pygame.draw module through PYTHONPATH. SDL2 dummy video/audio match Base and Gold. Four actual official test/... IDs are parsed from anchored terminal status lines.

The active native DrawRectTest runs the complete upstream added test_rect__draw_line_width: a 100x100 surface, 80x50 rectangle, line width 10, 40 white corner diagonal samples and four black inner corners. Three unchanged neighboring methods cover filled rectangles, one-pixel lines and the width-omitted default. Commented PythonDrawRectTest is not executed. Original inputs/assertions are unchanged. Float anti-aliasing, every clipping case and other shape algorithms are not claimed as reproduced defects.

Image source identity, setup literal version 2.1.1.dev1, native module path/hash and pinned SDL 2.0.14 header/runtime dependencies are audited. NumPy and external image fixtures are not required. Runtime assets are mounted only during evaluation.
