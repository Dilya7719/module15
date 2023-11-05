from django import template


register = template.Library()


CENSOR_WORDS_LIST = [
   'образование',
   'матч',
   'анчелотти',
   'тренер',
   'природа'
]


@register.filter(name='censor')
def news_filter(text: str):
   """
   text: текст, к которому нужно применить фильтр
   """
   text_split = text.split()

   for i, word in enumerate(text_split):
      if word[0].lower() + word[1:] in CENSOR_WORDS_LIST:
         text_split[i] = word[0] + (len(word) - 1) * '*'

   return ' '.join(text_split)