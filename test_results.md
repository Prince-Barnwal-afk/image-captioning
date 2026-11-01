
# Image Captioning — Initial Test Results

Model: Salesforce/blip-image-captioning-base

| Test | Image category | Generated caption | Main subject correct? | Notes |
|---|---|---|---|---|
| 1 | Animal | a dog with its mouth open and tongue out| main object is corret but it tongue is not out | tongue is not out | 
| 2 | Person | a woman standing in an office| true| no need  |
| 3 | Vehicle | the ford mustang is shown in this image| true | no need  |
| 4 | Outdoor scene | a man standing on a balcony looking out at the mountains| there is also a women | women is not detected  |
| 5 | Multiple objects | man sitting on the ground with his dog| true | both man and dog and ground detected |

## Observations

- Number of images tested: 5
- Successful caption generations: 5/5
- Incorrect or incomplete captions:
  - Test 1: The caption incorrectly stated that the dog's tongue was out.
  - Test 4: The caption detected the man and mountains but missed the woman.
- Errors encountered: None

## Conclusion

The pretrained BLIP model generated captions for all five test images. It generally identified the main subjects correctly, but it sometimes described details incorrectly or missed objects in a scene. Further evaluation is needed to assess its performance more systematically.
