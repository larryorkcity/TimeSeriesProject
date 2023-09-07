
from app import app
from flask import jsonify
from .analysis import analyze_population_data

@app.route('/population_dashboard', methods=['GET'])
def get_population_dashboard():
    # 분석된 대시보드 데이터 가져오기
    dashboard_data = analyze_population_data()

    return jsonify(dashboard_data)

# More Addtional Routers
# 더 많은 라우트들을 추가할 수 있습니다.
    
