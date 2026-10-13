# Analysis

Source Case 57 maps to benchmark Case 058. Base b21508798ab548ed90eb4d6bf01db14b880c9c91 is the verified first parent of merge d3a3b6dddba4af1153aa6c01be6d3be5f43636ca. The exact product patch changes only Python JpegImagePlugin.py: APP14 color transform reads payload index 11 instead of 1 and handles IndexError specifically. The exact protected upstream test patch includes test_file_jpeg.py and the binary JPEG fixture.

Base fails the official APP14 test with AssertionError: assert 100 == 1 on the RGB adobe_transform metadata. It reads the ASCII d byte at payload index 1 instead of the transform at index 11. Both unchanged JPEG decoding and CMYK roundtrip regressions pass. Gold passes all three nodes without skips, including RGB transform 1, CMYK transform 2 and absent transform for the shortened APP14 payload. Product changes are Python-only; no native C defect is independently established.

Original source row 57 records incorrect result/output and a mixed APP/JPEG read/ImImagePlugin/ImageSequence/PNG/WalImageFile/native ImagingSplit chain. These remain original source metadata, not this official APP14 metadata test trace. This run observes AssertionError for adobe_transform 100 instead of 1 in Python JPEG metadata parsing; native C runtime presence does not prove a native C defect.

The exact upstream APP14 test checks RGB transform 1, CMYK transform 2 and absence of transform for the shortened fixture. Two unchanged regressions cover normal JPEG decoding and CMYK roundtrip. The official 29342-byte JPEG fixture is preserved by an exact binary patch and audited against its upstream blob and SHA256. Its declared APP14 segment length is 13 bytes including the 2-byte length field, leaving an 11-byte payload with no index 11. The upstream comment is preserved verbatim. Product changes are Python-only.

Source Python-C classification is retained under the existing source-classification, official-test and commit-deduplication rule. This verifies Python metadata parsing, without independently establishing a native C defect.

GitHub REST API opening: 2021-04-15T11:14:33Z; merge: 2021-04-25T08:36:41Z. UTC date fields remain separate. Source: https://api.github.com/repos/python-pillow/Pillow/pulls/5408.
