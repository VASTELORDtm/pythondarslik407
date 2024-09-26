# id = ['S001', 'S002', 'S003', 'S004']
# Isimlar = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# raqamlar = [85, 98, 89, 92]
#
# result = []
#
# for i in range(len(id)):
#     student_dict = {id[i]: {Isimlar[i]: raqamlar[i]}}
#     result.append(student_dict)
#
# print(result)
# input = 'hammayo_tanish_bilish'
#
# result = {}
#
# for char in input:
#     if char in result:
#         result[char] += 1
#     else:
#         result[char] = 1
#
# print(result)
# def sozlarni_almashtirish(input):
#     output = input.copy()
#
#     for key in range(1, len(input) + 1, 2):
#         if key + 1 in input:
#             output[key] = input[key + 1]
#             output[key + 1] = input[key]
#
#     return output
#
# dict1 = {1: 'ABC', 2: 'DEF', 3: 'GHI', 4: 'JKL', 5: 'MNO'}
#
# result = sozlarni_almashtirish(dict1)
# print(result)
# def alohida_sozlar(input):
#     demak = input.split('. ')
#
#     sozlar = []
#     for b in demak:
#         b = b.strip('.')
#         sozlar.extend(b.split())
#
#     return sozlar, demak
#
#
# a = "Salom Yoz. Olam juda ham go'zal. Imtihon bo'lyapti."
#
# sozlar_royxati, sozlar = alohida_sozlar(a)
#
# print("sozlar:", sozlar_royxati)
# print("jumlalar:", sozlar)
# def eng_katta_raqamlar(son_royxati):
#     saralangan_sozlar = sorted(map(str, son_royxati), reverse=True)
#
#     sonlar = ''.join(saralangan_sozlar)
#     return sonlar
#
# input1 = [1, 2, 3]
# input2 = [61, 228, 9]
#
# output1 = eng_katta_raqamlar(input1)
# output2 = eng_katta_raqamlar(input2)
#
# print(output1)
# print(output2)
# def list_to_dict(input_list):
#     natija_dict = {}
#
#     for narsalar in input_list:
#         kallit = narsalar[0]
#         sozlar = narsalar[1:]
#         natija_dict[kallit] = sozlar
#
#     return natija_dict
#
# input_sana = [
#     [1, 'Jean Castro', 'V'],
#     [2, 'Lula Powell', 'V'],
#     [3, 'Brian Howell', 'VI'],
#     [4, 'Lynne Foster', 'VI'],
#     [5, 'Zachary Simon', 'VII']
# ]
#
# output = list_to_dict(input_sana)
# print(output)
# def raqamni_filtirlash(son_royxati):
#     natija = []
#
#     for son in son_royxati:
#         birinchi_digit = str(son)[0]
#
#         if int(birinchi_digit) % 2 == 0:
#             natija.append(son)
#
#     return natija
#
#
# input_sana = [123, 456, 789, 852, 12, 42, 61, 369]
#
# def sonlarni_hariflash(son):
#     if son == 0:
#         return "nol"
#
#     birliklar = ["", "bir", "ikki", "uch", "to'rt", "besh", "olti", "yetti", "sakkiz", "to'qqiz"]
#     onliklar = ["", "on", "o'n bir", "o'n ikki", "o'n uch", "o'n to'rt", "o'n besh", "o'n olti", "o'n yetti", "o'n sakkiz", "o'n to'qqiz"]
#     onlar = ["", "", "yigirma", "ottiz", "qiriq", "ellik", "oltmish", "yetmish", "sakson", "to'qson"]
#     yuzlar = ["", "ming", "million", "milliard"]
#
#     sozlar = []
#
#     def convert_chunk(n):
#         if n < 10:
#             return birliklar[n]
#         elif n < 20:
#             return onliklar[n - 10]
#         elif n < 100:
#             onlik_qismi = n // 10
#             birlik_qismi = n % 10
#             return onlar[onlik_qismi] + (" " + birliklar[birlik_qismi] if birlik_qismi else "")
#         elif n < 1000:
#             yuzlar_qismi = n // 100
#             dam_olish = n % 100
#             return birliklar[yuzlar_qismi] + " yuz" + (" " + convert_chunk(dam_olish) if dam_olish else "")
#
#     bolakni_hisoblash = 0
#     while son > 0:
#         bolak = son % 1000
#         if bolak > 0:
#             sozlar.append(convert_chunk(bolak) + (" " + yuzlar[bolakni_hisoblash] if yuzlar[bolakni_hisoblash] else ""))
#         son //= 1000
#         bolakni_hisoblash += 1
#
#     return ' '.join(reversed(sozlar)).strip()
#
# input_raqam = int(input("Sonni kiriting (1-1000000000): "))
#
# if 1 <= input_raqam <= 1000000000:
#     output = sonlarni_hariflash(input_raqam)
#     print(output)
# else:
#     print("Iltimos, 1 dan 1000000000 gacha bo'lgan sonni kiriting.")