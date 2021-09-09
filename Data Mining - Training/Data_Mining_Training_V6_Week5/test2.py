from sklearn.model_selection import train_test_split
from sklearn.datasets import load_files
from transformers import TFAutoModel, AutoTokenizer
from vncorenlp import VnCoreNLP

# Tao file
reviews = load_files(r"E:\PycharmProjects\Data Mining - Training\Data_Mining_Training_V6_Week2"
                     r"\combined_for_cross_validation", encoding="utf16")
files, categories = reviews.data, reviews.target

# Segment File cho Phobert
rdrsegmenter = VnCoreNLP(r"E:\PycharmProjects\venv\Lib\site-packages\vncorenlp\VnCoreNLP-1.1.1.jar",
                         annotators="wseg", max_heap_size='-Xmx500m')
new_files = []
for file in files:
    new_sentence = []

    new_file = rdrsegmenter.tokenize(file)
    for sentence in new_file:
        new_sentence.extend(sentence)

    new_files.append(new_sentence)
# file: type(str)
# Làm đẹp da bằng củ quả Dù ăn vào hay đắp lên da, các loại rau quả đều có ích cho bạn. Chẳng hạn, với hàm lượng
# vitamin A, C, B6 phong phú, cà chua giúp tế bào niêm mạc sinh trưởng khoẻ mạnh, làm sáng da và ngừa nếp nhăn. Nhiều
# loại củ quả khác cũng rất hữu ích như cà rốt chứa vitamin A, C và carotene, nuôi dưỡng tế bào da, ngừa mụn. Quả
# chanh làm nhạt sắc tố do có thành phần của vitamin C. Dưa leo chứa kẽm, làm khít lỗ chân lông... Sau đây là một số
# ứng dụng cụ thể: - 1 quả cà chua, 1 lòng trắng trứng gà, nửa cốc đường cát trắng. Cắt cà chua thành từng khoanh,
# băm nhỏ. Khuấy tan lòng trắng trứng với đường. Cho cà chua vào hỗn hợp lòng trắng trứng và đường, trộn đều. Rửa
# sạch mặt, thoa hỗn hợp lên, massage nhẹ khoảng 5-10 phút. Tác dụng: Ngừa mụn, làm sáng, bảo vệ da. - Nửa củ cà rốt,
# nửa cốc dầu ngô, 2 miếng vải gạc y tế, 1 khăn lông.Cà rốt cắt khoanh, giã nhuyễn, cho vào miếng gạc, gói lại. Thấm
# miếng gạc vào trong dầu ngô thoa nhẹ lên mặt, massage ít phút. Dùng khăn nóng lau mặt. Tác dụng: Làm mờ vết thâm do
# mụn để lại, tạo độ ẩm cho làn da khô. - 5 giọt nước cốt chanh, 3-4 thìa cà phê đường cát vàng, 1-2 thìa cà phê nước
# ấm. Cho nước cốt chanh vào trong đường cát, thêm 1-2 muỗng nước ấm vào. Thoa hỗn hợp lên mặt 15-20 phút, để khô,
# rửa mặt sạch. Tác dụng: Làm giảm hắc tố trên da. - Nửa quả dưa leo, nửa quả chanh vắt lấy nước, 2 muỗng mật ong,
# 50 ml sữa đặc. Cắt dưa leo thành lát, xay mịn. Cho mật ong vào sữa đặc, khuấy đều. Cho nước cốt chanh và dưa leo
# vào hỗn hợp. Đắp mặt nạ lên mặt trong 15-20 phút, rửa sạch. Tác dụng: Cân bằng độ ẩm, làm khít lỗ chân lông.

# new_sentence: type list
# ['Làm_đẹp', 'da', 'bằng', 'củ', 'quả', 'Dù', 'ăn', 'vào', 'hay', 'đắp', 'lên', 'da', ',', 'các', 'loại', 'rau',
# 'quả', 'đều', 'có_ích', 'cho', 'bạn', '.', 'Chẳng_hạn', ',', 'với', 'hàm_lượng', 'vitamin', 'A', ',', 'C', ',',
# 'B6', 'phong_phú', ',', 'cà_chua', 'giúp', 'tế_bào', 'niêm_mạc', 'sinh_trưởng', 'khoẻ_mạnh', ',', 'làm', 'sáng',
# 'da', 'và', 'ngừa', 'nếp', 'nhăn', '.', 'Nhiều', 'loại', 'củ', 'quả', 'khác', 'cũng', 'rất', 'hữu_ích', 'như',
# 'cà_rốt', 'chứa', 'vitamin', 'A', ',', 'C', 'và', 'carotene', ',', 'nuôi_dưỡng', 'tế_bào', 'da', ',', 'ngừa',
# 'mụn', '.', 'Quả', 'chanh', 'làm', 'nhạt', 'sắc_tố', 'do', 'có', 'thành_phần', 'của', 'vitamin', 'C.', 'Dưa_leo',
# 'chứa', 'kẽm', ',', 'làm', 'khít', 'lỗ_chân_lông', '...', 'Sau', 'đây', 'là', 'một_số', 'ứng_dụng', 'cụ_thể', ':',
# '-', '1', 'quả', 'cà_chua', ',', '1', 'lòng_trắng', 'trứng', 'gà', ',', 'nửa', 'cốc', 'đường_cát', 'trắng', '.',
# 'Cắt', 'cà_chua', 'thành', 'từng', 'khoanh', ',', 'băm', 'nhỏ', '.', 'Khuấy', 'tan', 'lòng_trắng', 'trứng', 'với',
# 'đường', '.', 'Cho', 'cà_chua', 'vào', 'hỗn_hợp', 'lòng_trắng', 'trứng', 'và', 'đường', ',', 'trộn', 'đều', '.',
# 'Rửa', 'sạch', 'mặt', ',', 'thoa', 'hỗn_hợp', 'lên', ',', 'massage', 'nhẹ', 'khoảng', '5-10', 'phút', '.',
# 'Tác_dụng', ':', 'Ngừa', 'mụn', ',', 'làm', 'sáng', ',', 'bảo_vệ', 'da', '.', '-', 'Nửa', 'củ', 'cà_rốt', ',',
# 'nửa', 'cốc', 'dầu', 'ngô', ',', '2', 'miếng', 'vải', 'gạc', 'y_tế', ',', '1', 'khăn', 'lông.Cà', 'rốt', 'cắt',
# 'khoanh', ',', 'giã', 'nhuyễn', ',', 'cho', 'vào', 'miếng', 'gạc', ',', 'gói', 'lại', '.', 'Thấm', 'miếng', 'gạc',
# 'vào', 'trong', 'dầu', 'ngô', 'thoa', 'nhẹ', 'lên', 'mặt', ',', 'massage', 'ít', 'phút', '.', 'Dùng', 'khăn',
# 'nóng', 'lau', 'mặt', '.', 'Tác_dụng', ':', 'Làm', 'mờ', 'vết', 'thâm', 'do', 'mụn', 'để', 'lại', ',', 'tạo',
# 'độ_ẩm', 'cho', 'làn', 'da', 'khô', '.', '-', '5', 'giọt', 'nước_cốt', 'chanh', ',', '3-4', 'thìa_cà_phê',
# 'đường_cát', 'vàng', ',', '1-2', 'thìa_cà_phê', 'nước', 'ấm', '.', 'Cho', 'nước_cốt', 'chanh', 'vào', 'trong',
# 'đường_cát', ',', 'thêm', '1-2', 'muỗng', 'nước', 'ấm', 'vào', '.', 'Thoa', 'hỗn_hợp', 'lên', 'mặt', '15-20',
# 'phút', ',', 'để', 'khô', ',', 'rửa', 'mặt', 'sạch', '.', 'Tác_dụng', ':', 'Làm', 'giảm', 'hắc', 'tố', 'trên',
# 'da', '.', '-', 'Nửa', 'quả', 'dưa_leo', ',', 'nửa', 'quả', 'chanh', 'vắt', 'lấy', 'nước', ',', '2', 'muỗng',
# 'mật_ong', ',', '50', 'ml', 'sữa', 'đặc', '.', 'Cắt', 'dưa_leo', 'thành', 'lát', ',', 'xay', 'mịn', '.', 'Cho',
# 'mật_ong', 'vào', 'sữa', 'đặc', ',', 'khuấy', 'đều', '.', 'Cho', 'nước_cốt', 'chanh', 'và', 'dưa_leo', 'vào',
# 'hỗn_hợp', '.', 'Đắp', 'mặt_nạ', 'lên', 'mặt', 'trong', '15-20', 'phút', ',', 'rửa', 'sạch', '.', 'Tác_dụng', ':',
# 'Cân_bằng', 'độ_ẩm', ',', 'làm', 'khít', 'lỗ_chân_lông', '.']

train_files, val_files, train_labels, val_labels = train_test_split(new_files, categories)
# print(len(train_files)) 19674
# print(len(val_files)) 6558
# print(len(train_labels)) 19674
# print(len(val_labels)) 6558
tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base", use_fast=False)

train_encodings = tokenizer(train_files, padding=True, truncation=True, return_tensors="tf")
# ValueError: too many values to unpack (expected 2)
