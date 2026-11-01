from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# الصفحة الرئيسية للموقع
@app.route('/')
def home():
    return render_template('index.html')

# المسار الخاص باستقبال طلب الانضمام ومعالجته بـ Python
@app.route('/join', methods=['POST'])
def join_scout():
    # استلام البيانات القادمة من نموذج الموقع
    data = request.get_json()
    
    name = data.get('name')
    phone = data.get('phone')
    message = data.get('message')
    
    # التأكد من وضوح واكتمال البيانات
    if not name or not phone:
        return jsonify({'status': 'error', 'message': 'يرجى كتابة الاسم ورقم الهاتف!'}), 400

    # يمكنك هنا حفظ البيانات في ملف نصي على السيرفر (كقاعدة بيانات بسيطة)
    with open('members.txt', 'a', encoding='utf-8') as f:
        f.write(f"الاسم: {name} | الهاتف: {phone} | الرسالة: {message}\n")
    
    # طباعة البيانات في شاشة الترميز (Terminal) لتراها بنفسك
    print(f"NEW MEMBER JOINED: {name} - {phone}")

    # إرجاع رد إلى الموقع بنجاح الإرسال
    return jsonify({
        'status': 'success',
        'message': f'أهلاً بك يا بطل ({name})! تم تسجيل طلب انضمامك بنجاح وسنتواصل معك قريباً ⚜️'
    })

if __name__ == '__main__':
    # تشغيل السيرفر المحتوي على بايثون
    app.run(debug=True, port=5000)