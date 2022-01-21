in_file = open("%s.ini" % version, 'r', encoding='utf-8')
data1 = in_file.read().split("\n")  # 以换行符为分割点将数据分割为列表
in_file.close()
d1_shiftx = int(data1[remove_line[0]-1])
d1_bg_color = data1[remove_line[1]-1]
d1_word_color = data1[remove_line[2]-1]
d1_bgtm_if = int(data1[remove_line[3]-1])
d1_frm3 = int(data1[remove_line[4]-1])
d1_select_if = int(data1[remove_line[5]-1])
d1_Window_width = int(data1[remove_line[6]-1])
d1_frm1 = int(data1[remove_line[7]-1])
d1_frm2 = int(data1[remove_line[8]-1])
d1_shiftx_new = d1_shiftx
del data1