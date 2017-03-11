import pkgutil
import re

languages_re = {}
known_languages = ["da", "de", "en", "es", "fi", "fr", "hu",
                   "it", "nl", "no", "pt", "ru", "sv", "tr"]


def calc(sentence, langs, extras, sniff_length):
    sentence = sentence.strip()
    sentence = sentence[:sniff_length]
    scores = {}
    total = 0
    for lang in langs:
        if lang not in languages_re:
            languages_re[lang] = get_re(lang, extras)
        lang_re = languages_re[lang]
        score = 0
        # can deal with large data
        for _ in lang_re.finditer(sentence):
            score += 1
            total += 1
        scores[lang] = score
    if not scores:
        return {"lang": None, "probabilities": {}}
    total = sum(scores.values())
    if not total:
        return {"lang": None, "probabilities": {}}
    lang = max(scores, key=lambda x: scores[x])
    probs = {k: v * 1. / total for k, v in scores.items()}
    return {"lang": lang, "probabilities": probs}


def get_re(lang, extras):
    words = pkgutil.get_data("nltk_data", "{}.lang".format(lang.lower()))
    words = [x for x in words.decode("utf8").split("\n") if x]
    if extras is not None:
        words = words + extras[lang]
    r = r"\b" + r"\b|\b".join(words) + r"\b"
    r = re.compile(r, flags=re.IGNORECASE)
    return r


def fastlang(sentence, languages=None, extras=None, sniff_length=1000):
    languages = known_languages if languages is None else languages
    return calc(sentence, languages, extras, sniff_length)


def accuracy(sentences, truths, languages=None):
    languages = known_languages if languages is None else languages
    preds = [fastlang(x, languages)["lang"] for x in sentences]
    score = [x == y for x, y in zip(preds, truths)]
    return sum(score) * 1. / len(score)


def main():
    import sys
    print(fastlang(" ".join(sys.argv[1:])))

if __name__ == "__main__":
    main()
