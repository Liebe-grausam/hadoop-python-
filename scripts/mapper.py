import sys
import re
import jieba

def process_data(data):
    # 在这里对数据进行处理，比如去除非中文字符，并分词
    content = re.sub(r'[^\u4e00-\u9fa5]', '', data)  # 去除非中文字符
    words = jieba.cut(content)  # 分词
    return words

def main():
    stop_words = set()
    with open('stopwords.txt', 'r', encoding='utf-8') as f:
        for line in f:
            stop_words.add(line.strip())
    for line in sys.stdin:
        words = process_data(line.strip())
        for word in words:
            if word not in stop_words:  
                print(f"{word}\t1")

if __name__ == "__main__":
    main()

