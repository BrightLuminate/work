from flask import Blueprint, render_template

#Blueprint로 crud 앱을 생성한다.
crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static",
)

# index 엔드포인트를 작젓ㅇ하고 index.html을 반환한다.
@crud.route("/")    #@app.route("/crud/") 원래는 이거이다.
def index():
    return render_template("crud/index.html")