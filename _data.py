# ★このサービスの独自コンテキスト（品質向上のため必ず参照）:
# 解決する問題: 睡眠時間・眠りの深さ・日中の眠気などから睡眠の質を診断し改善アドバイスを提案
# 対象ユーザー: 健康管理に取り組むアクティブな方
# キーワード: 睡眠
TITLE = '睡眠の質チェッカー【無料】無料診断・アドバイス'
DESCRIPTION = '睡眠時間・眠りの深さ・日中の眠気などから睡眠の質を診断し改善アドバイスを提案。登録不要・完全無料でご利用いただけます。'
DESCRIPTION_SHORT = '睡眠時間・眠りの深さ・日中の眠気などから睡眠の質を診断し改善アドバイスを提案...'
COLOR1 = '#FFEDD5'
COLOR2 = '#FFF7ED'
COLOR_BTN = '#EA580C'
FOOTER_LINKS = [('https://appadaycreator.com/stretch-timer/', 'ストレッチタイマー・記録ツール'), ('https://appadaycreator.com/mental-health-checker/', 'メンタルヘルス・ストレスチェック'), ('https://appadaycreator.com/morning-routine-planner/', '朝ルーティン最適化ツール')]

CUSTOM_CSS = """"""

# MAIN_HTML≤100行 / 色=#EA580C / class="card"でUI / id="result"で結果隠し
MAIN_HTML = """<div class="card" id="quiz-start">
  <h2 style="font-size:18px;font-weight:700;margin-bottom:12px;">😴 睡眠の質セルフチェック</h2>
  <p style="color:#666;font-size:14px;margin-bottom:8px;">睡眠時間・寝つき・日中の眠気から睡眠の質を診断します</p>
  <ul style="font-size:13px;color:#94a3b8;margin:0 0 16px 16px;"><li>質問数：5問</li><li>所要時間：約1分</li></ul>
  <button class="btn" onclick="startQuiz()">診断スタート →</button>
</div>
<div id="quiz-area" style="display:none;">
  <div style="font-size:12px;color:#999;margin-bottom:8px;">質問 <span id="q-num">1</span> / <span id="q-total">5</span></div>
  <div id="q-progress" style="height:4px;background:#e5e7eb;border-radius:2px;margin-bottom:16px;">
    <div id="q-bar" style="height:100%;background:#6366F1;border-radius:2px;transition:width .3s;width:20%;"></div>
  </div>
  <p id="q-text" style="font-size:16px;font-weight:600;margin-bottom:16px;"></p>
  <div id="q-options"></div>
</div>
<div class="result" id="result">
  <div class="card">
    <h3 id="r-title" style="font-size:18px;font-weight:700;margin-bottom:8px;color:#6366F1;"></h3>
    <p id="r-desc" style="color:#444;font-size:14px;line-height:1.7;"></p>
    <button class="btn" style="margin-top:16px;" onclick="location.reload()">もう一度診断</button>
  </div>
</div>"""

# JS: スタブの TODO コメント箇所を実装してください（骨格は変えないこと）
JS_CODE = """const QUESTIONS = [
  { text:'Q1. 平均的な睡眠時間は？', opts:['5時間未満','5〜6時間','6〜7時間','7時間以上'] },
  { text:'Q2. 寝つきはどうですか？', opts:['布団に入ってすぐ眠れる','10〜20分程度','30分〜1時間かかる','1時間以上眠れないことが多い'] },
  { text:'Q3. 夜中に目が覚めますか？', opts:['ほとんど起きない','たまに（月数回）','よく起きる（週3〜4回）','毎晩何度も目が覚める'] },
  { text:'Q4. 日中の眠気・だるさは？', opts:['ほとんどない','ランチ後に少し眠い程度','午後かなり眠くなる','常に眠くて仕事に集中できない'] },
  { text:'Q5. 朝の目覚め感は？', opts:['すっきり爽快','まあまあ（普通）','ぼんやり・重だるい','非常につらく起きるのがしんどい'] },
];
const RESULTS = [
  { title:'✨ 良質睡眠タイプ — 素晴らしい睡眠習慣です', desc:'睡眠の質・量ともに良好です。この状態を維持するために、就寝・起床時刻を週末も含めて一定に保つ「睡眠リズム」を大切に。スマホの就寝1時間前のブルーライト制限、就寝前の軽いストレッチや入浴（38〜40℃・15分）を続けることでさらに質を向上できます。' },
  { title:'😪 睡眠負債タイプ — 慢性的な睡眠不足に注意', desc:'睡眠時間が不足しています。平日の睡眠不足を週末に「寝だめ」で補う習慣はサーカディアンリズムを乱し逆効果です。毎日同じ時刻に起きる「起床時刻固定」から始めましょう。就寝1〜2時間前のカフェイン摂取を避け、15分の昼寝（パワーナップ）を取り入れることで日中のパフォーマンスも改善します。' },
  { title:'🌙 入眠困難タイプ — 寝つきを改善しましょう', desc:'布団に入ってもなかなか眠れない状態です。「眠れない」というプレッシャーが眠れなさを悪化させています。①就寝30分前からスマホを見ない ②腹式呼吸（4-7-8呼吸法）で自律神経を落ち着ける ③眠れない場合は一度起きて読書など ④毎朝同じ時刻に起床して体内時計をリセット。2週間改善しない場合は睡眠外来への相談を検討してください。' },
  { title:'⚠️ 睡眠障害疑いタイプ — 専門家への相談を推奨', desc:'中途覚醒・日中の強い眠気・起床困難は睡眠時無呼吸症候群・不眠症・むずむず脚症候群などの睡眠障害のサインかもしれません。これらは治療で大きく改善する疾患です。睡眠外来・内科・心療内科での相談をお勧めします。パートナーにいびきを確認してもらい（無呼吸の有無）、睡眠日誌をつけて受診時に持参すると診断の助けになります。' },
];
function getResult(answers) {
  const total = answers.reduce((s,a) => s+a.idx, 0);
  if(total <= 3) return RESULTS[0];
  if(total <= 7) {
    const a = answers.map(x=>x.idx);
    return a[1] >= 2 ? RESULTS[2] : RESULTS[1];
  }
  if(total <= 12) return RESULTS[2];
  return RESULTS[3];
}
const BTN='#6366F1'; let cur=0; const ans=[];
document.addEventListener('DOMContentLoaded',()=>{ document.getElementById('q-total').textContent=QUESTIONS.length; });
function startQuiz(){ cur=0;ans.length=0; document.getElementById('quiz-start').style.display='none'; document.getElementById('quiz-area').style.display='block'; document.getElementById('result').classList.remove('show'); renderQ(); }
function renderQ(){
  const q=QUESTIONS[cur];
  document.getElementById('q-num').textContent=cur+1;
  document.getElementById('q-bar').style.width=((cur+1)/QUESTIONS.length*100)+'%';
  document.getElementById('q-text').textContent=q.text;
  document.getElementById('q-options').innerHTML=q.opts.map((o,i)=>`<button onclick="answer(${i})" style="width:100%;padding:12px;margin-bottom:8px;border:2px solid #e5e7eb;border-radius:10px;font-size:14px;cursor:pointer;background:#fff;text-align:left;">${o}</button>`).join('');
}
function answer(idx){ ans.push({idx}); cur++; if(cur>=QUESTIONS.length) showResult(); else renderQ(); }
function showResult(){
  document.getElementById('quiz-area').style.display='none';
  const r=getResult(ans);
  document.getElementById('r-title').textContent=r.title;
  document.getElementById('r-desc').textContent=r.desc;
  document.getElementById('result').classList.add('show');
}"""

FAQ = [
    ("睡眠の質チェッカーは無料で使えますか？", "はい、完全無料でご利用いただけます。登録・ログイン・アプリのインストールも不要です。"),
    ("何回でも診断できますか？", "はい、何度でもご利用いただけます。条件を変えて繰り返し診断してみてください。"),
    ("スマートフォンでも使えますか？", "はい、スマートフォン・タブレット・PCすべてのデバイスに対応しています。"),
    ("診断結果は保存されますか？", "結果はブラウザには保存されません。スクリーンショットやSNSシェアでご記録ください。"),
    ("入力したデータはサーバーに送信されますか？", "いいえ。すべての処理はブラウザ内で完結し、個人情報・入力データのサーバー送信は行いません。"),
]

HOW_TO = [
    "ページを開き、診断の説明を確認する",
    "スタートボタンをクリックして診断を開始する",
    "表示される質問に順番に回答する（約1〜2分）",
    "すべて回答すると診断結果が自動表示される",
    "結果のアドバイスを確認してSNSでシェアする",
]

