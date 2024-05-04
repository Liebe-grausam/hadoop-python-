from collections import defaultdict
import sys

def reducer():
    current_word = None
    current_count = 0
    word_count_dict = defaultdict(int)

    # 读取来自Mapper的输入
    for line in sys.stdin:
        word, count = line.strip().split('\t')
        
        # 转换计数为整数类型
        try:
            count = int(count)
        except ValueError:
            # 如果无法转换，就跳过这一行
            continue
        
        # 合并相同的单词并计算总次数
        if current_word == word:
            current_count += count
        else:
            # 输出累积的单词计数
            if current_word:
                word_count_dict[current_word] += current_count
            current_word = word
            current_count = count

    # 处理最后一个单词
    if current_word == word:
        word_count_dict[current_word] += current_count

    # 输出最终结果
    for word, count in word_count_dict.items():
        print(f"{word}\t{count}")

if __name__ == "__main__":
    reducer()
