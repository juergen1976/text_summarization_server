from flask import Flask
from logic.SummarizeLogic import SummarizeLogic
from flask import abort, jsonify, request
import json

server = Flask(__name__)
logic = SummarizeLogic()

@server.route("/summary/<id>")
def getTextSummary(id):
  doc_id, text_summary = logic.getTextSummarize(id)
  if (doc_id is None):
    abort(404)
  return jsonify({'document_id': doc_id,
                     'summary': text_summary})

@server.route('/summary', methods=['POST'])
def update_record():
    payload = json.loads(request.data)
    if payload["text"] is None:
      abort(400)
    generated_doc_id, _ = logic.summarizeTextAndStore(payload["text"])

    return generated_doc_id

server.run()