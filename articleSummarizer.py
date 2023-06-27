from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from newspaper import Article



def summarize(text):
    summaryText=[]
    # Initialize the parser with the input text
    parser = PlaintextParser.from_string(text, Tokenizer("english"))

    # Choose the summarization algorithm (e.g., LexRank)
    summarizer = LexRankSummarizer()
    
    # Specify the number of sentences in the summary
    summary_length = 2

    # Generate the summary
    summary = summarizer(parser.document, summary_length)

    for sentence in summary:
        summaryText.append(sentence)

    summary_text = ' '.join(map(str, summaryText))
    return summary_text;


    






