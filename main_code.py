# print(file_finder('C:/Users/hp/Desktop/html/html'))
# C:/Users/hp/Desktop/taxi
import os, shutil
import pdb
# import codecs
# import re
folder_path = input("Enter Folder Path:=")
folderpath = folder_path.replace('\\','/')
main_path = folderpath + '/index.html'
# ===== First Method =================================
# g = codecs.open(r''+main_path, 'r')
# f = g.read()
# start = f.find("<!doctype html>")
# # start = start
# end =  f.find("</header>")
# end = end + 9
# paragraphs = f[start:end]
# print(paragraphs)
# g.close()
#================= Second Method ====================
isFile = os.path.isfile(folderpath+'/default.blade.php')
if isFile == False:
	results = []
	for html_files in os.listdir(folderpath):
		if html_files.endswith('.html'):
			results.append(html_files)
	for all_html_names_in_folder in results:
		with open(r''+folderpath+'/'+all_html_names_in_folder,'r',encoding='utf-8') as html_open:
			without_extension_filename = os.path.splitext(all_html_names_in_folder)[0]
			with open(r''+folderpath+'/'+without_extension_filename+'.blade.php','w') as write_html_file:
				read_html_file = html_open.read()

				start_html = read_html_file.find('</header>')
				start_html = start_html + 9
				if start_html != -1:
					end_html = read_html_file.find('<footer')
					if end_html == -1:
						print("Dekho Bhai  </header>  File Me Nahi Hai..")
					else:
						line_1 = "@extends('layouts/default')"
						line_2 = "@section('title') @parent @stop"
						line_3 = "@section('header_styles')"
						line_4 = '@stop'
						line_5 = "@section('meta')"
						line_6 = '@stop'
						line_7 = "@section('content')"
						line_8 = '@stop'
						line_9 = "@section('footer_scripts')"
						line_10 = '@stop'
						all_code = read_html_file[start_html:end_html]
						write_html_file.write('\n'+line_1+'\n'+line_2+'\n'+line_3+'\n'+line_4+'\n'+line_5+'\n'+line_6+'\n'+line_7+'\n'+all_code+'\n'+line_8+'\n'+line_9+'\n'+line_10)
		
	with open(r''+main_path,'r',encoding='utf-8') as page:
		with open(r''+folderpath+'/default.blade.php','w') as def_page:
			read_file = page.read()
			start = read_file.find('<!doctype html>')
			start_2 = read_file.find('<footer')
			end_0 = read_file.find('</head>')
			end = read_file.find('</header>')
			end_1 = read_file.find('</body>')
			end_2 = read_file.find('</html>')
			# pdb.set_trace()
			if start == -1:
				other_condition = read_file.find('<!DOCTYPE html>')
				if other_condition != -1:
					start = other_condition
				else:
					print("Please Start Your Index.html With <!doctype html>")						
			if end == -1 and end_2 == -1 and end_0 == -1:
				print("Dekho  Header,</html>,</head>ya </body> File Me Nahi Hai..")
			else:
				yield_1 = "@yield('header_styles')"
				yield_2 =  "@yield('content')"
				yield_3 = "@yield('footer_scripts')"
				end = end + 9
				end_2 = end_2 + 7
				add_head = end_0 - 3
				add_body = end_1 - 3
				staring_code = read_file[start:end_0]
				staring_code2 = read_file[add_head:end]
				ending_code = read_file[start_2:end_1]
				ending_code2 = read_file[add_body:end_2]
				def_page.write(staring_code + '\n'+yield_1 + staring_code2 + '\n' + yield_2 +'\n'+ ending_code+'\n'+yield_3+'\n'+ending_code2)
				print("Check Your Folder All Files Change Successfully...")
			# else:
			# 	print("Kuch Bhi Ho Abhi Ke Liye Index File Me Starting  <!doctype html> Se Karo Yr..")
else:
	print("Bhai Yaha default.blade.php File Pahele Se He Hai...")

A =	input()






















