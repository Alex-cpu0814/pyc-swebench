# Analysis

Source Case 56 maps to benchmark Case 057. Base f0679aff4d43dbd595b98501dc7a8420550bf4e8 is the verified first parent of merge 5f39e8e60ae0662b850484b2ad7a1eaa83677dd3. The exact product patch adds signed big-endian si16be in Python _binary.py and uses it for the PSD layer count in Python PsdImagePlugin.py. The protected test includes the unchanged upstream test_file_psd.py diff and binary negative_layer_count.psd fixture.

Base fails the official frame-count test with PIL.UnidentifiedImageError when Image.open reads the valid negative_layer_count.psd fixture. Both unchanged normal PSD regressions pass. Gold passes all three official nodes without skips. No hang was observed; the product patch changes Python signed-count parsing only and does not establish a native C defect.

Original source row 56 records hang and a mixed JPEG read/container seek/WalImageFile/native _split call chain. These remain original source metadata, not this official PSD test trace. This run observes PIL.UnidentifiedImageError opening the negative-count PSD, with no hang. The product patch changes Python parsing only; native C runtime presence does not prove a native C defect.

The source Python-C taxonomy is preserved under the existing classification, official-test and commit-deduplication rule. This case verifies a Python parsing regression in a native-code runtime.

The GitHub REST API records PR opening at 2021-07-15T09:18:35Z and merge at 2021-07-28T09:53:24Z. UTC opening and merge dates remain separate. Source: https://api.github.com/repos/python-pillow/Pillow/pulls/5613.
