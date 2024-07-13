import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

# Health Check
@app.route('/health', methods=['GET'])
def health():
    return jsonify(status='UP')

# 레코드 생성
@app.route('/records', methods=['POST'])
def create_record():
    data = request.get_json()
    new_record = Record(name=data['name'])
    db.session.add(new_record)
    db.session.commit()
    return jsonify(id=new_record.id, name=new_record.name)

# 모든 레코드 조회
@app.route('/records', methods=['GET'])
def get_records():
    records = Record.query.all()
    return jsonify(records=[{'id': record.id, 'name': record.name} for record in records])

# 특정 레코드 조회
@app.route('/records/<int:id>', methods=['GET'])
def get_record(id):
    record = Record.query.get(id)
    if record is None:
        return jsonify(error="레코드를 찾을 수 없음"), 404
    return jsonify(id=record.id, name=record.name)

# 특정 레코드 수정
@app.route('/records/<int:id>', methods=['PUT'])
def update_record(id):
    data = request.get_json()
    record = Record.query.get(id)
    if record is None:
        return jsonify(error="레코드를 찾을 수 없음"), 404
    record.name = data['name']
    db.session.commit()
    return jsonify(id=record.id, name=record.name)

# 특정 레코드 삭제
@app.route('/records/<int:id>', methods=['DELETE'])
def delete_record(id):
    record = Record.query.get(id)
    if record is None:
        return jsonify(error="레코드를 찾을 수 없음"), 404
    db.session.delete(record)
    db.session.commit()
    return jsonify(message="레코드가 삭제됨")

if __name__ == '__main__':
    # 데이터베이스 초기화
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8080)
