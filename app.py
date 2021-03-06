from flask import Flask, request

from AnswerRetriever import AnswerRetriever
from GoogleUrlExtractor import GoogleUrlExtractor
app = Flask(__name__)


@app.errorhandler(Exception)
def server_error(err):
	app.logger.exception(err)
	return str(err), 500


@app.route('/answer/', methods=['GET'])
def get_answer():
	question = request.args.get('question')
	url = request.args.get('url')
	ar = AnswerRetriever()
	# ar.upload_question_and_url(url, question)
	return ar.get_answer(question, url)


@app.route('/', methods=['GET'])
def get_wiki_pages():
	question = request.args.get('question')
	url_extractor = GoogleUrlExtractor()
	if question is None or question == '':
		raise Exception("Can't take empty string for question")
	urls = url_extractor.extract_answer_urls(question)
	return {'result': urls}


if __name__ == '__main__':
	app.run()
