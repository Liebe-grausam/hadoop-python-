from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud(word_freq):
    word_cloud = WordCloud(font_path="HARMONYOS SANS SC.TTF",background_color='white', width=1000, height=700, max_words=50)
    word_cloud.generate_from_frequencies(word_freq)
    plt.figure(figsize=(10, 7))
    plt.imshow(word_cloud, interpolation="bilinear")
    plt.axis('off')
    plt.savefig('wordcloud.png')
    plt.show()


def main():
    word_freq = {}  # 词频数据
    with open("output.txt", "r", encoding="utf-8") as file:
        for line in file:
            word, freq = line.strip().split("\t")
            word_freq[word] = int(freq)

    generate_wordcloud(word_freq)

if __name__ == "__main__":
    main()

