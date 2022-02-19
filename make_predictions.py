import requests

from config import nya_url

_emoji_by_preds = {
    'sentiment': {
        'positive': '😛',
        'neutral': '😐',
        'negative': '😠'
    },
    'toxic': {
        'no toxic': '🤔',
        'toxic': '🤬'
    }
}


def emoji_by_preds(preds, target):
    l, e = max(_emoji_by_preds[target].items(), key=lambda t: preds[t[0]])
    return e


async def make_predictions(text):
    r = requests.get(
        url=f'{nya_url}/api/predict/?input=manual&text={text}',
        params={
            'input': 'manual',
            'text': text,
            'toxic': 'toxic/SkolkovoInstitute/russian_toxicity_classifier',
            'sentiment': 'sentiment/blanchefort/rubert-sentiment'
        }
    )

    r.raise_for_status()
    data = r.json()

    return {
        'toxic': emoji_by_preds(data['toxic'], 'toxic'),
        'sentiment': emoji_by_preds(data['sentiment'], 'sentiment'),
    }
