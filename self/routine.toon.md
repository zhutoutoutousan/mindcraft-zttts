schema: self/routine
note: Daily hygiene and preventive-care particulars. Not a Person vertex. Not a diagnosis. Tips need SOURCE. Do not invent last_done dates. Clinic streets and insurance numbers stay in .private/.
tz: Europe/Berlin
updated: 2026-09-06T17:30:00+02:00
protocol.note: When the human asks 今天干什么 / what should I do today, merge this store into Today with training fog learn calendar. Empty PROBE stays empty. Medical intervals are reminders to confirm with a clinician, not prescriptions.

daily[]{id,slot,label,label_zh,active,minutes,protocol,source}:
  brush-am,morning,Brush teeth,刷牙,true,3,"Soft brush 2 minutes. Spit; do not rinse hard immediately if using fluoride toothpaste (common public tip — confirm product label).",https://www.ada.org/resources/research/science-and-research-institute/oral-health-topics/toothbrushes
  face-am,morning,Wash face,洗脸,true,2,"Lukewarm water; gentle cleanser if used. Do not invent a skincare brand stack.",,
  shower-or-body,morning,Body wash / shower,洗澡清洁,true,10,"As needed. Stop if skin barrier is raw. Particulars stay private.",,
  brush-pm,evening,Brush teeth,刷牙,true,3,"Same as morning. If floss/interdental once daily; evening preferred in many dental education pages.",https://www.ada.org/resources/research/science-and-research-institute/oral-health-topics/floss
  floss,evening,Floss / interdental,牙线或牙缝清洁,true,3,"Once daily. Technique matters more than brand. Bleeding that persists → ask dentist; do not self-diagnose.",https://www.ada.org/resources/research/science-and-research-institute/oral-health-topics/floss
  face-pm,evening,Wash face,洗脸,true,2,"Remove sunscreen/sweat. Moisturize if dry. No invented actives.",,
  tidy-surface,evening,Clear one surface,简单收拾,true,5,"One tray or desk plane. Habit stacking after brush-pm.",,

periodic[]{id,label,label_zh,interval_months,last_done,next_due,status,source,note}:
  dental-checkup,Dental checkup / exam,牙医检查,6,,,open,https://www.ada.org/resources/research/science-and-research-institute/oral-health-topics/toothbrushes,"Many adults use ~6-month recall; actual interval is clinician-set. Log last_done when human reports a visit. Do not invent a clinic appointment."
  dental-cleaning,Professional cleaning (prophy),洗牙/洁治,6,,,open,https://www.nidcr.nih.gov/health-info/tooth-decay,"Often paired with exam. Frequency varies by risk. Reminder only until last_done is set."
  dental-hygiene-review,Home-care technique review,刷牙牙线手法复查,12,,,open,https://www.ada.org/resources/research/science-and-research-institute/oral-health-topics/floss,"Ask hygienist to watch brush/floss once a year if unsure."
  gp-checkup,Primary-care / GP checkup,全科体检,12,,,open,,"Interval is personal. Do not invent labs. Put named Arzt in .private/."
  skin-check,Skin check if indicated,皮肤检查(如有指征),12,,,open,,"Only if human or clinician flagged moles/ulcers. Not a default scare."
  vision-screen,Vision screen,视力筛查,24,,,open,,"If screens all day; interval personal."

tip[]{id,topic,text,source,added}:
  fluoride-spit,brush,"After fluoride toothpaste, spit; avoid immediate full rinse so fluoride stays. Label wins over tip.",https://www.ada.org/resources/research/science-and-research-institute/oral-health-topics/toothpastes,2026-09-06
  soft-bristle,brush,"Soft bristles; hard scrubbing can harm gums/enamel. Replace brush ~every 3 months or when splayed.",https://www.ada.org/resources/research/science-and-research-institute/oral-health-topics/toothbrushes,2026-09-06
  tongue-optional,brush,"Tongue cleaning is optional adjunct; not a substitute for brush+interdental.",https://www.ada.org/resources/research/science-and-research-institute/oral-health-topics/toothbrushes,2026-09-06

optimize[]{id,habit,change,why,status,source}:
  stack-floss-pm,floss,Do floss immediately after brush-pm,Same cue reduces skip rate. Behavioral stacking — not medical.,open,human 2026-09-06
  timer-brush,brush-am,Use 2-minute timer or brush song,Duration under-shoot is common.,open,https://www.ada.org/resources/research/science-and-research-institute/oral-health-topics/toothbrushes

log[]{date,id,done,note}:
  2026-09-06,seed,true,Store created. No daily completions invented.

agentHints[6]:
  - When asked 今天干什么 include due periodic + active daily slots + one optimize open item if any.
  - Never invent last_done or a booked Termin. Human reports visits.
  - Mouth ulcer / fog stack particulars stay in .private/health.fu.md — do not copy sites here.
  - cron/routine-enrich may APPEND tip[] with SOURCE URL only. No diagnosis CLAIM.
  - Due periodic with empty last_done → status open remind ask-human.
  - Do not add Chinese as native. Reply in the user's current language.
