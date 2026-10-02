from pathlib import Path
import re,json,html

repo=Path(__file__).resolve().parents[1]
old=(repo/'cheatsheet.html').read_text(encoding='utf-8-sig')
basefile=repo/'tools'/'reference-content.html'
if not basefile.exists():
    fragment=old[old.index('<h2>1'):old.rindex('</div>\n</body>')]
    fragment=fragment.replace('אין מחיר → הזמנה להציע הצעות','מחיר ניתן לחישוב (למשל מחירון) מספיק; חסר עיקרי שלא ניתן לקביעה → אין הצעה')
    fragment=re.sub(r'<tr><td><b>59</b>.*?</tr>','',fragment,flags=re.S)
    fragment=fragment.replace('8 · ריבוי חייבים ונושים','8 · ריבוי חייבים - חלק כללי 54–56')
    fragment=fragment.replace('11 · נוסחי סעיפים מרכזיים (לצטט מילה במילה)','11 · סעיפים נבחרים ולשון החוק')
    fragment=fragment.replace("<b>4–5.</b> פעולת קטין", "<b>4–5 (תמצית).</b> פעולת קטין")
    fragment=fragment.replace("<b>ס' 18</b> — סיכול. יסוד אי-הצפיות כמעט תמיד נכשל בישראל", "<b>תרופות ס' 18</b> - סיכול: בדקו אי-צפיות, אי-יכולת למנוע והשינוי בקיום; שם האירוע לבדו אינו מכריע")
    fragment=fragment.replace('15 · לוח בקרה אחרון — 10 דקות לפני שמגישים','15 · לוח בקרה לפני הגשה')
    fragment=fragment.replace('האם אני בתוך <b>מגבלת העמודים</b>? (חריגה — לא נבדקת בכלל)','האם אני בתוך <b>מגבלת הכתיבה שבגליון הבחינה</b>?')
    fragment=fragment.replace('האם כל נימוק הוא <b>עד שתי שורות</b> וכולל מספר סעיף?', 'האם כל נימוק עומד <b>במגבלת השורות שבהוראות</b> וכולל מספר סעיף ושם החוק?')
    basefile.write_text(fragment,encoding='utf-8')
else: fragment=basefile.read_text(encoding='utf-8')
fragment=fragment.replace('מסוימות</b> — אם אין מחיר, זו הזמנה','מסוימות</b> - מחיר נקוב או ניתן לקביעה; אל תשללו הצעה רק מפני שלא כתבו סכום')
fragment=fragment.replace('תניה גורפת</b> — ס\' 6 סיפא, אין לה תוקף. אך בדקו הפרה יסודית <b>מסתברת', 'תניה גורפת</b> - תרופות 6 סיפא: אין לה תוקף אלא אם הייתה סבירה בעת הכריתה. בדקו גם הפרה יסודית <b>מסתברת')
fragment=fragment.replace('בכל דיון על פיצויים.', 'בדיון על פיצויים לפי 10, 12 או 13; הוא אינו חל על מסלולי 11 ו-15.')
fragment=fragment.replace('<td><b>תשובה נ\' בר נתן</b></td><td>3(א)</td>', '<td><b>תשובה נ\' בר נתן</b></td><td>3(ב)</td>')
fragment=fragment.replace('בישראל טענת סיכול כמעט תמיד נכשלת ביסוד <b>אי-הצפיות</b> — מלחמות, מגפות ותנודות מחירים נחשבות צפויות.', 'המרצה מדגישה שקשה להוכיח <b>אי-צפיות</b>. בכל קייס בודקים מה היה צפוי בעת הכריתה, מה ניתן היה למנוע וכיצד השתנה הקיום; לא מכריעים לפי שם האירוע בלבד.')
basefile.write_text(fragment,encoding='utf-8')

css='''
.exam-ref{font-family:"Segoe UI",Arial,sans-serif;color:#172331;background:#fff;font-size:16px;line-height:1.6;max-width:1000px;margin:auto;padding:22px}
.exam-ref *{box-sizing:border-box}.exam-ref h1{font-size:26px;margin:0 0 7px;color:#183e63}.exam-ref h2{font-size:21px;margin:22px 0 10px;border-bottom:2px solid #b9cbdc;padding-bottom:7px;break-after:avoid}
.exam-ref h3{font-size:18px;margin:17px 0 7px;break-after:avoid}.exam-ref .law-tag{font-size:13px;padding:3px 7px;background:#eaf0f6;border:1px solid #becddd;border-radius:4px;display:inline-block;margin-inline-start:8px;white-space:nowrap}
.exam-ref table{width:100%;min-width:0;border-collapse:collapse;font-size:15px;margin:9px 0 16px}.exam-ref th,.exam-ref td{border:1px solid #b6c2ce;padding:8px 10px;text-align:right;vertical-align:top;overflow-wrap:break-word}.exam-ref th{background:#eaf0f6;color:#183e63}.exam-ref tr{break-inside:avoid}.exam-ref thead{display:table-header-group}
.exam-ref .caseText,.exam-ref .statute{white-space:pre-wrap}.exam-ref .statute{font-family:Arial,sans-serif;font-size:16px;line-height:1.7}.exam-ref .two{column-count:1}
.exam-ref .box,.exam-ref .warn{padding:12px 15px;border-inline-start:4px solid #183e63;background:#f0f4f8;margin:12px 0;break-inside:avoid}.exam-ref .warn{border-color:#806029;background:#fbf6ec}
.exam-ref .ref-topics{display:flex;flex-wrap:wrap;gap:7px;margin:12px 0}.exam-ref .ref-topics a,.exam-ref .ref-results a{border:1px solid #b6c6d8;border-radius:5px;background:#f5f8fc;padding:7px 11px;color:#183e63;text-decoration:none}
.exam-ref .ref-topics a:hover,.exam-ref .ref-results a:hover{background:#dae7f4}.exam-ref .ref-tools{padding:12px;background:#eef3f8;border:1px solid #c0d0e1;border-radius:8px;position:sticky;top:0;z-index:3}.exam-ref .ref-search-form{display:flex;gap:8px;align-items:center}.exam-ref .ref-search{width:100%;min-width:0;font:inherit;padding:10px;border:1px solid #7894b0;border-radius:5px;background:#fff;color:#172331}.exam-ref button{font:inherit;border:1px solid #547da7;border-radius:5px;background:#183e63;color:#fff;padding:10px 14px;cursor:pointer}.exam-ref .ref-status{display:block;font-size:13px;color:#3e5369;margin-top:6px}.exam-ref .ref-results{display:flex;flex-direction:column;gap:5px;max-height:220px;overflow:auto;margin-top:6px}.exam-ref .ref-results:empty{display:none}
.exam-ref .ref-actions{display:flex;gap:12px;flex-wrap:wrap;align-items:center;margin:12px 0}.exam-ref .ref-actions a{font-weight:700;color:#183e63}.exam-ref .ref-meta{font-size:14px;color:#3e5369}.exam-ref [data-ref-route],.exam-ref .exam-section{scroll-margin-top:140px}.exam-ref .ref-target{outline:3px solid #94702b;outline-offset:4px}.exam-ref tr.ref-target{outline-offset:-2px}.exam-ref .ref-back{display:block;text-align:left;font-size:13px;margin:10px 0}.exam-ref .pb{break-before:auto}
#v-ref .exam-ref{padding:0;max-width:none}#v-ref .exam-ref .ref-tools{position:static}#v-ref .exam-ref [data-ref-route],#v-ref .exam-ref .exam-section{scroll-margin-top:80px}
@media(max-width:620px){.exam-ref{padding:14px;font-size:16px}.exam-ref th,.exam-ref td{padding:7px 6px}.exam-ref table{font-size:14px}.exam-ref h2{font-size:19px}.exam-ref .ref-tools{position:static}.exam-ref .exam-section{scroll-margin-top:20px}.exam-ref .law-tag{white-space:normal}.exam-ref .ref-topics a{font-size:14px}}
@media print{.exam-ref{font-size:10.5pt;line-height:1.45;padding:0;max-width:none;color:#000}.exam-ref .noprint{display:none!important}.exam-ref h1{font-size:18pt}.exam-ref h2{font-size:13pt}.exam-ref h3{font-size:11.5pt}.exam-ref table{font-size:10.5pt}.exam-ref th,.exam-ref td{padding:5pt 6pt}.exam-ref .statute{font-size:10.5pt}.exam-ref .law-tag{font-size:9pt}.exam-ref .box,.exam-ref .warn{background:#fff;border:1px solid #888}.exam-ref .ref-target{outline:none}@page{size:A4;margin:13mm 12mm}}
'''

lawlabels={1:'סדר כתיבה',2:'חלק כללי',3:'חלק כללי',4:'חלק כללי',5:'חלק כללי',6:'חלק כללי',7:'חלק כללי',8:'חלק כללי',9:'תרופות',10:'פסיקה',11:'שם החוק מעל כל נוסח',12:'כתיבה',13:'איתור סוגיה',14:'בדיקת תשובה',15:'בדיקת תשובה'}
route_data={
 1:('שלד תשובה - יסוד, יישום, מסקנה וסעד','סדר ניתוח כתיבה לחץ זמן'),
 2:('חלק כללי 1–11 - הצעה וקיבול','חרטה משלוח מסירה איחור שתיקה הצעה בלתי הדירה מחירון'),
 3:('חלק כללי - זיכרון דברים','רבינאי רביניי נוסחת קשר חתימה מקדמה מסוימות 26'),
 4:('חלק כללי 12 - תום לב במשא ומתן','הסתמכות קיום קל בניין גילוי משא ומתן מו מ'),
 5:('חלק כללי 14–21 - פגמים ברצון','טעות הטעיה כפייה כפיה טעות סופר 14 15 16 17 19 20 21 ידיעה ביטול עצמאי בית משפט'),
 6:('חלק כללי 17 - כפייה כלכלית','רחמים אקספומדיה שושנה קרן לחץ איומים אזהרה אלטרנטיבה'),
 7:('חלק כללי 27, 29 - חוזה על תנאי','מתלה מפסיק היתר רישיון לא התקיים 27 29'),
 8:('חלק כללי 54–56 - ריבוי חייבים','יחד ולחוד חלוקה פנימית חזרה הפטר ביטול אין אפשרות להיפרע 54 55 56'),
 10:('פסקי דין - שם, סעיף והכלל','פסיקה אסמכתא תושיה תושייה פרץ ביטון אוסי איינשטיין קלמר סויסה'),
 11:('נוסחים נבחרים - לפי שם החוק','נוסח ציטוט לשון חוק מילולי'),
 12:('ניסוחים מוכנים - להתאים לעובדות','פתיחת תשובה משפט נימוק אסמכתא'),
 13:('דגלים אדומים - מילים בעובדות','לזהות סוגיה קייס אירוע סימנים'),
 14:('טעויות נפוצות - בדיקה מהירה','מלכודות טעויות בלבול'),
 15:('לפני הגשה - בדיקת תשובה','בדיקה אחרונה שורות עמודים זמן הגשה')}
parts=re.split(r'(?=<h2\b)',fragment)
sections=[]
for part in parts:
    if not part.strip():continue
    number=int(re.search(r'<h2[^>]*>(\d+)',part).group(1))
    ident=f'exam-sec-{number:02d}'
    part=re.sub(r'<h2(?: class="pb")?>', '<h2>',part,count=1)
    if number==1: part=re.sub(r'<h2>.*?</h2>','<h2>1 · שלד תשובה - מנתחים רק מה שנשאל</h2>',part,count=1)
    part=part.replace('</h2>',f' <span class="law-tag">{lawlabels[number]}</span></h2>',1)
    if number in {2,5,7,8,9}:
        law='תרופות' if number==9 else 'חלק כללי'
        part=re.sub(r'(<tr><th[^>]*>)([^<]*)(</th>)',lambda m:m.group(1)+law+': '+m.group(2)+m.group(3),part)
    attrs=f'id="{ident}" class="exam-section" data-exam-section="{number}"'
    if number in route_data:
        title,keywords=route_data[number]
        attrs+=f' data-ref-route="{title}" data-ref-keywords="{keywords}"'
    if number==9:
        remedies=[('א. אכיפה','exam-enforcement','תרופות 2–3 - אכיפה','חריגים אישי בלתי צודקת בר ביצוע 2 3'),('ב. ביטול','exam-cancellation','תרופות 6–9 - ביטול והשבה','יסודית ארכה הודעה זמן סביר ביטול חלקי 6 7 8 9'),('ג. פיצויים','exam-damages','תרופות 10–15 - פיצויים והקטנת נזק','נזק צפיות שווי ביום ביטול מוסכם חילוט עוגמת נפש תושיה תושייה 10 11 13 14 15'),('ד. הפרה','exam-frustration','תרופות 17–18 - הפרה צפויה וסיכול','סיכול צפיות מלחמה מגפה מגיפה אי אפשר למנוע השבה שיפוי 17 18')]
        for prefix,rid,title,keywords in remedies:
            part=re.sub(r'<h3>('+re.escape(prefix)+r'[^<]*)</h3>',f'<h3 id="{rid}" data-ref-route="{title}" data-ref-keywords="{keywords}">\\1</h3>',part,count=1)
    if number==11:
        part=part.replace('</h2>','</h2><p class="ref-meta">קטעים נבחרים. כותרת החוק קובעת לאיזה חוק שייך כל מספר. „תמצית” היא הסבר, ולא ציטוט מילולי; לנוסח מלא השתמשו בקובץ החקיקה של המרצה.</p>',1)
    if number in {2,5,8,9}:
        row_law='תרופות' if number==9 else 'חלק כללי'
        def statute_row(match):
            raw=match.group(1)
            text=re.sub('<[^>]+>',' ',raw)
            text=html.unescape(text)
            found=re.search(r'\b(\d+)\s*(?:\(([א-ת0-9])\))?',text)
            if not found:return match.group(0)
            identpart=found.group(1)+(found.group(2) or '')
            label=(found.group(1)+('('+found.group(2)+')' if found.group(2) else ''))
            subjects={('חלק כללי','14א'):'טעות ידועה וביטול עצמאי',('חלק כללי','14ב'):'טעות בלתי ידועה ופנייה לבית המשפט',('חלק כללי','15'):'הטעיה',('חלק כללי','19'):'ביטול חלקי בפגם בכריתה',('תרופות','7א'):'ביטול בהפרה יסודית',('תרופות','7ב'):'ארכה בהפרה לא יסודית',('תרופות','7ג'):'ביטול חלקי בהפרה',('תרופות','14א'):'נטל הקטנת הנזק',('תרופות','14ב'):'שיפוי הוצאות להקטנת הנזק',('תרופות','18א'):'סיכול - שלושה יסודות',('תרופות','18ב'):'השבה ושיפוי בסיכול',('חלק כללי','55ב'):'ביטול חיוב אחד החייבים',('חלק כללי','55ג'):'הפטר לאחד החייבים',('חלק כללי','56ג'):'אין אפשרות להיפרע מחייב'}
            subject=subjects.get((row_law,identpart),'סעיף '+label)
            rid='exam-'+('remedies' if number==9 else 'general')+'-'+identpart
            title=html.escape(row_law+' '+label+' - '+subject,quote=True)
            return f'<tr id="{rid}" data-ref-route="{title}" data-ref-keywords="{html.escape(subject,quote=True)}">'+raw+'</tr>'
        part=re.sub(r'<tr>(<td>.*?)</tr>',statute_row,part,flags=re.S)
    if number==10:
        part=re.sub(r"(<td>)ת' ([^<]+)(</td>)",r'\1תרופות \2\3',part)
        part=re.sub(r'(<td>)(\d[^<]*)(</td>)',r'\1חלק כללי \2\3',part)
        part=part.replace('חלק כללי 12 / מקרקעין 8','חלק כללי 12; מקרקעין 8')
        def case_row(match):
            case_row.counter+=1
            name=html.escape(re.sub('<[^>]+>','',match.group(1)),quote=True)
            return f'<tr id="exam-case-{case_row.counter:02d}" data-ref-route="פסק דין: {name}" data-ref-keywords="פסיקה אסמכתא"><td>{match.group(1)}</td>'
        case_row.counter=0
        part=re.sub(r'<tr><td>(<b>[^<]+</b>)</td>',case_row,part)
    sections.append(f'<section {attrs}>\n{part}\n<a class="ref-back noprint" href="#exam-start">חזרה למפתח ↑</a>\n</section>')

opening='''<div class="exam-ref" id="exam-start">
<h1>דף עזר למסכם - למצוא מהר, לכתוב מדויק</h1>
<p class="ref-meta">עודכן 2.10.2026 · חומרי הקורס שלנו · חלק כללי ותרופות הם שני חוקים שונים</p>
<div class="ref-actions noprint"><a href="https://bohanyzahal-cyber.github.io/bar-ilan-legal-aspects/output/pdf/exam-reference.pdf">הורדת ערכת PDF להדפסה - עם מפתח ומספרי עמודים</a></div>
<div class="ref-tools noprint"><form class="ref-search-form"><label for="exam-search">איתור:</label><input class="ref-search" id="exam-search" type="search" placeholder="למשל: תרופות 14, ארכה, תושיה" autocomplete="off"><button type="submit">מצא</button></form><span class="ref-status" role="status" aria-live="polite">חפשו נושא, סעיף עם שם החוק או פסק דין. מקש / לחיפוש; Esc לניקוי.</span><div class="ref-results"></div></div>
<nav class="ref-topics noprint" aria-label="מפתח דף העזר">
<a href="#exam-sec-01">שלד תשובה</a><a href="#exam-sec-02">כריתה</a><a href="#exam-sec-05">פגמים ברצון</a><a href="#exam-sec-07">תנאים</a><a href="#exam-sec-08">ריבוי חייבים</a><a href="#exam-enforcement">אכיפה</a><a href="#exam-cancellation">ביטול</a><a href="#exam-damages">פיצויים</a><a href="#exam-frustration">סיכול</a><a href="#exam-sec-10">פסקי דין</a><a href="#exam-sec-11">לשון החוק</a><a href="#exam-sec-15">לפני הגשה</a></nav>
<div class="box"><b>כשנתקעים:</b> מזהים את המילה בעובדות → פותחים את הנושא → בודקים יסודות → כותבים יישום ומסקנה עם שם החוק וסעיף. אם החיפוש לא התקדם, מסמנים את תת־השאלה וממשיכים; חוזרים בזמן שהקציתם לבדיקה.</div>
<div class="warn"><b>שלוש הבחנות לפני כל ציטוט:</b> חלק כללי 14 = טעות; תרופות 14 = הקטנת נזק. חלק כללי 17 = כפייה; תרופות 17 = הפרה צפויה. תרופות 18 = סיכול; עושק לפי 18 לחלק הכללי הוצא מהמבחן אצלנו.</div>
<p class="ref-meta">מגבלת הזמן והכתיבה נקבעות בגליון הבחינה. חומר פתוח אושר; סוג חומרי העזר והשימוש באמצעים דיגיטליים עדיין טעונים בירור. גרסת ה-PDF עובדת גם ללא חיבור לרשת.</p>
'''
body=opening+'\n'.join(sections)+'</div>'
js=(repo/'tools/reference-tools.js').read_text(encoding='utf-8')
html='<!DOCTYPE html>\n<html lang="he" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>דף עזר למסכם - היבטים משפטיים בניהול</title><style>body{margin:0;background:#f4f6f8}'+css+'</style></head><body>'+body+'<script>'+js+'\nExamReference.init(document.querySelector(".exam-ref"));</script></body></html>'
(repo/'cheatsheet.html').write_text(html,encoding='utf-8')
index=(repo/'index.html').read_text(encoding='utf-8-sig')
index=re.sub(r'<script id="exam-reference-tools">.*?</script>\s*','',index,flags=re.S)
index=index.replace('\n  if(v==="ref") ExamReference.init($("refBody").querySelector(".exam-ref"));','')
start=index.index('const REF_HTML = ');end=index.index('\n/* ==================== APP',start)
embedded='<style>'+css+'</style>'+body.replace('<table>','<table class="ref">')
index=index[:start]+'const REF_HTML = '+json.dumps(embedded,ensure_ascii=False)+';\n'+index[end:]
index=index.replace('$("refBody").innerHTML = REF_HTML;', '$("refBody").innerHTML = REF_HTML;')
needle='  if(v==="ref" && !$("refBody").innerHTML)'
line_start=index.index(needle);line_end=index.index('\n',line_start)
index=index[:line_end]+ '\n  if(v==="ref") ExamReference.init($("refBody").querySelector(".exam-ref"));'+index[line_end:]
index=index.replace('<b>זה הדף שלוקחים לבחינה.</b> כאן הוא לקריאה מהירה.', '<b>חומר עזר למבחן המסכם.</b> מפתח וחיפוש לנושאים, סעיפים ופסקי דין. סוג חומרי העזר המותרים נקבע בהוראות הבחינה.')
index=index.replace('(Ctrl+P, מומלץ דו-צדדי).', ' · <a href="https://bohanyzahal-cyber.github.io/bar-ilan-legal-aspects/output/pdf/exam-reference.pdf">ערכת PDF עם מפתח עמודים</a>.')
first_script=index.index('<script>')
index=index[:first_script]+'<script id="exam-reference-tools">'+js+'</script>\n'+index[first_script:]
(repo/'index.html').write_text(index,encoding='utf-8')
print('Prepared standalone and embedded reference: 15 indexed sections, 4 remedies routes, individual case routes.')
