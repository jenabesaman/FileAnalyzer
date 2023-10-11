# import cv2
# from transformers import TrOCRProcessor, VisionEncoderDecoderModel
# import requests
# from PIL import Image
#
# processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
# model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")
#
# # load image from the IAM dataset
#
# # url = "https://fki.tic.heia-fr.ch/static/img/a01-122-02.jpg"
# # image = Image.open(requests.get(url, stream=True).raw).convert("RGB")
#
#
# IMAGE_PATH ="C:/Workarea/File_Analyser/etc/not_melli/english.jpg"
#
# custom_characters = {'0': '٠', '5': '٥'}
# image = cv2.imread(IMAGE_PATH)
#
# pixel_values = processor(image, return_tensors="pt").pixel_values
# generated_ids = model.generate(pixel_values)
#
# generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
# print(generated_text)
# import cv2
# from transformers import (
#     TrOCRConfig,
#     TrOCRProcessor,
#     TrOCRForCausalLM,
#     ViTConfig,
#     ViTModel,
#     VisionEncoderDecoderModel,
# )
# import requests
# from PIL import Image
#
# # TrOCR is a decoder model and should be used within a VisionEncoderDecoderModel
# # init vision2text model with random weights
# encoder = ViTModel(ViTConfig())
# decoder = TrOCRForCausalLM(TrOCRConfig())
# model = VisionEncoderDecoderModel(encoder=encoder, decoder=decoder)
#
# # If you want to start from the pretrained model, load the checkpoint with `VisionEncoderDecoderModel`
# processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
# model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")
#
# # load image from the IAM dataset
# # url = "https://fki.tic.heia-fr.ch/static/img/a01-122-02.jpg"
# # image = Image.open(requests.get(url, stream=True).raw).convert("RGB")
#
# IMAGE_PATH ="C:/Workarea/File_Analyser/etc/not_melli/english.jpg"
# image=cv2.imread(IMAGE_PATH)
# pixel_values = processor(image, return_tensors="pt").pixel_values
# text = "industry, ' Mr. Brown commented icily. ' Let us have a"
#
# # training
# model.config.decoder_start_token_id = processor.tokenizer.cls_token_id
# model.config.pad_token_id = processor.tokenizer.pad_token_id
# model.config.vocab_size = model.config.decoder.vocab_size
#
# labels = processor.tokenizer(text, return_tensors="pt").input_ids
# outputs = model(pixel_values, labels=labels)
# loss = outputs.loss
# round(loss.item(), 2)
#
# # inference
# generated_ids = model.generate(pixel_values)
# generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
# print(generated_text)
#
#
# from PIL import Image
# from trocr.src.main import TrocrPredictor
#
# # load images
# image_names = ["data/img1.png", "data/img2.png"]
# images = [Image.open(img_name) for img_name in image_names]
#
# # directly predict on Pillow Images or on file names
# model = TrocrPredictor()
# predictions = model.predict_images(images)
# predictions = model.predict_for_file_names(image_names)
#
# # print results
# for i, file_name in enumerate(image_names):
#     print(f'Prediction for {file_name}: {predictions[i]}')

from ArabicOcr import arabicocr
image_path="C:/Workarea/File_Analyser/etc/not_melli/1234.jpg"
out_image='out.jpg'
results=arabicocr.arabic_ocr(image_path,out_image)
