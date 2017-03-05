# fastlang

Fast Detection of Language without Dependencies

For a list of the supported languages, see: https://github.com/kootenpv/fastlang/tree/master/nltk_data

## Usage

From the command line:

```python
fastlang some sentence you want to predict the language of
# {'lang': 'en', 'probabilities': {'ru': 0.0, 'pt': 0.0, 'fr': 0.0, 'it': 0.0, 'es': 0.0, 'tr': 0.0, 'en': 0.7142857142857143, 'de': 0.0, 'da': 0.0, 'nl': 0.2857142857142857, 'hu': 0.0, 'no': 0.0, 'sv': 0.0, 'fi': 0.0}}
fastlang "including with special characters :)"
# {'lang': 'en', 'probabilities': {'pt': 0.0, 'sv': 0.0, 'ru': 0.0, 'nl': 0.0, 'hu': 0.0, 'fi': 0.0, 'it': 0.0, 'en': 1.0, 'da': 0.0, 'tr': 0.0, 'es': 0.0, 'no': 0.0, 'fr': 0.0, 'de': 0.0}}
```
In Python:

```python
from fastlang import fastlang
# default
fastlang("I want to predict something")

# fastlang(sentence, languages, sniff_length)
# sniff length is limiting how many characters to search, default=1000
fastlang("I want to predict something", ["en", "nl"], sniff_length=300)
```

### Caveats

Only works with text that contains stopwords. Frequent other words such as "cat" and "dog" won't help for prediction, only words like "the", "he", "with" etc.

It's more of a toy implementation. A recommended lib would be: https://github.com/Mimino666/langdetect

### Credits:

Built upon the [nltk](http://www.nltk.org/book/ch02.html) stopwords, without depending on `nltk` itself.
