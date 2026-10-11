schema: self/nutrition
version: 1
tz: Europe/Berlin
updated: 2026-10-09T19:40:00+02:00
note: Meal log for this mindcraft only. Partner given names, contact, and health numbers stay out of this public store. Do not invent a TDEE. Label grams win over guesses.

privacy:
  publicRepo: true
  forbid[5]: given-names, email, phone, body-metrics, partner-health-urls
  partnerParticulars: .private/

shareRule: 2026-10-09 cups split 50/50; each person one identical protein drink. Order not logged.

conflictWithPartnerLog[3]:
  dinner,partner project logged a bowl meal this evening,this chat did not name a bowl
  drink,partner project logged a different flavour / guessed energy,label here is chocolate lactose-free yogurt drink 270g 161 kcal
  cups,partner project did not log these cups,this chat says both ate the cups equally

openQuestion: self/messages.toon.md outbound-2026-10-09-cups-vs-bowl

item[]{id,name,kind,pack_g,portion_note,kcal,protein_g,carb_g,fat_g,salt_g,source}:
  knorr-tomate-kaese,Knorr Nudeln in Tomaten-Käse-Sauce,cup,63,prepared portion 243g as labelled,227,8.3,43.3,2.0,1.4,label-photo-this-chat
  instant-huhn-asia,Instant-Nudeln asiatischer Art Hühnchengeschmack,cup,67,labelled portion 67g,289,7.0,36.9,11.7,4.26,label-photo-this-chat
  schoko-protein-270,laktosefreies Schoko-Joghurtgetränk 0.5% Fett,drink,270,one bottle RM 8% energy,161,23.4,15.0,1.4,0.46,label-photo-this-chat

meal[]{date,slot,who,status,items,kcal,protein_g,carb_g,fat_g,note}:
  2026-10-09,evening,self,logged,"0.5 knorr-tomate-kaese + 0.5 instant-huhn-asia + 1 schoko-protein-270",419,31.1,55.1,8.3,Human: each drank one same protein drink; cups eaten equally; order ignored
  2026-10-09,evening,partner,pending-other-chat,cups-share-unconfirmed,0,0,0,0,Other project chat already logged a dinner. Do not add cups or a second drink until that chat confirms. No given name here.

agentHints[6]:
  - Job first. Photos in this chat are the source for this person's items.
  - Partner state = the other project's latest chat publish, never a stale checkout in this workspace.
  - If the partner row is uncertain, ask that project. Do not overwrite its nutrition from here. Do not put a given name or contact in this public file.
  - 50/50 cups is the reading of "Becher gleich gegessen". Full cup each is not claimed.
  - Do not invent this person's bodyweight or TDEE. training.toon.md stays gitignored.
  - Magnesium / folate on the drink label are noted on the pack (max 1 bottle/day). Not a diagnosis.
