num = 248


def main():
    # txt存放路径
    txt_path = r"C:\Users\13289\Desktop\data.zhuv3\wav"

    with open('test.txt', encoding='utf-8') as f:
        all_lines = f.readlines()
        # for line in all_lines:

        # 写入语料
        count = 1
        for i in range(num):
            # 命名格式
            full_path = str(count)+'.txt'
            with open(full_path, 'w') as new_txt:
                # new_txt.write(line)
                new_txt.write(all_lines[count-1])
            print(all_lines[count-1])
            count += 1


if __name__ == '__main__':
    main()


