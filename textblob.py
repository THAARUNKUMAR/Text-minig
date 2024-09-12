from textblob import TextBlob
def predict_sent(text):
  blob=TextBlob(text)
  polarity=blob.sentiment.polarity
  if polarity>0:
    return "Good"
  elif polarity <0:
    return "Bad"
  else:
    return "Neutral"
def main():
  text=input("Enter the text: ")
  sentiment=predict_sent(text)
  print("The sentiment of the text is: ",sentiment)
main()
