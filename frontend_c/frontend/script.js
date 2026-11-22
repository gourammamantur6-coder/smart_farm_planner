"use strict";
/* ---------- i18n (Feature 3: local language) ---------- */
const T={
en:{app:"KrishiPlan",lang:"Language",user:"Sign in as",prob:"The problem",probtxt:"Farmers face unpredictable weather, crop diseases and poor soil. Guessing when to water wastes water and risks the crop.",users:"Built for farmers, farm workers, crop experts and suppliers.",
farm:"My farm",name:"Farm name",soil:"Soil type",crop:"Crop",area:"Area (acres)",moist:"Soil moisture (%)",plan:"Make water plan",
red:"Red loam",black:"Black clay",sand:"Sandy",ragi:"Ragi",paddy:"Paddy",maize:"Maize",
plan7:"7-day water plan",litres:"Litres per acre",total:"Total for farm",skip:"Skip",alerts:"Risk alerts",none:"No major risks this week.",
growth:"Crop growth (cm)",soilh:"Soil moisture trend (%)",yield:"Yield (tonnes/acre, last 5 seasons)",price:"Price trend (₹/quintal)",
speak:"Read aloud",saved:"Farm saved on this device",expert:"Crop expert view: read-only",only:"You can only see your own farm.",
fixname:"Enter a farm name (2–40 letters or numbers).",fixarea:"Area must be between 0.1 and 100 acres.",fixmoist:"Moisture must be 0 to 100.",
online:"Online",offline:"Offline – showing saved data",disc:"Advice is a guide based on sample data. Check with your local agriculture officer before acting.",
heat:"Heat above 38°C: water in early morning and evening.",rain:"Heavy rain expected: open drains to avoid waterlogging.",wind:"Strong wind: do not spray pesticides that day.",fung:"High humidity and warmth: check leaves for fungal disease.",
dry:"Dry spell with low soil moisture: irrigate in the first two days.",day:"Day"},
kn:{app:"ಕೃಷಿಪ್ಲಾನ್",lang:"ಭಾಷೆ",user:"ಬಳಕೆದಾರ",prob:"ಸಮಸ್ಯೆ",probtxt:"ಹವಾಮಾನ ಅನಿಶ್ಚಿತ, ಬೆಳೆ ರೋಗ ಮತ್ತು ಮಣ್ಣಿನ ಸಮಸ್ಯೆಗಳು ರೈತರಿಗೆ ಇವೆ. ಊಹೆಯಿಂದ ನೀರು ಹಾಕಿದರೆ ನೀರು ವ್ಯರ್ಥ, ಬೆಳೆಗೆ ಅಪಾಯ.",users:"ರೈತರು, ಕೃಷಿ ಕಾರ್ಮಿಕರು, ಬೆಳೆ ತಜ್ಞರು ಮತ್ತು ಪೂರೈಕೆದಾರರಿಗಾಗಿ.",
farm:"ನನ್ನ ಜಮೀನು",name:"ಜಮೀನಿನ ಹೆಸರು",soil:"ಮಣ್ಣಿನ ಪ್ರಕಾರ",crop:"ಬೆಳೆ",area:"ವಿಸ್ತೀರ್ಣ (ಎಕರೆ)",moist:"ಮಣ್ಣಿನ ತೇವಾಂಶ (%)",plan:"ನೀರಿನ ಯೋಜನೆ ಮಾಡಿ",
red:"ಕೆಂಪು ಮಣ್ಣು",black:"ಕಪ್ಪು ಮಣ್ಣು",sand:"ಮರಳು ಮಣ್ಣು",ragi:"ರಾಗಿ",paddy:"ಭತ್ತ",maize:"ಮೆಕ್ಕೆಜೋಳ",
plan7:"7 ದಿನಗಳ ನೀರಿನ ಯೋಜನೆ",litres:"ಪ್ರತಿ ಎಕರೆಗೆ ಲೀಟರ್",total:"ಒಟ್ಟು ಜಮೀನಿಗೆ",skip:"ಬೇಡ",alerts:"ಅಪಾಯ ಎಚ್ಚರಿಕೆಗಳು",none:"ಈ ವಾರ ದೊಡ್ಡ ಅಪಾಯವಿಲ್ಲ.",
growth:"ಬೆಳೆ ಬೆಳವಣಿಗೆ (ಸೆಂ.ಮೀ)",soilh:"ಮಣ್ಣಿನ ತೇವಾಂಶ ಪ್ರವೃತ್ತಿ (%)",yield:"ಇಳುವರಿ (ಟನ್/ಎಕರೆ, ಕಳೆದ 5 ಋತು)",price:"ಬೆಲೆ ಪ್ರವೃತ್ತಿ (₹/ಕ್ವಿಂಟಲ್)",
speak:"ಓದಿ ಹೇಳಿ",saved:"ಜಮೀನು ಈ ಸಾಧನದಲ್ಲಿ ಉಳಿಸಲಾಗಿದೆ",expert:"ಬೆಳೆ ತಜ್ಞರ ನೋಟ: ಓದಲು ಮಾತ್ರ",only:"ನಿಮ್ಮ ಜಮೀನು ಮಾತ್ರ ನೋಡಬಹುದು.",
fixname:"ಜಮೀನಿನ ಹೆಸರು ನಮೂದಿಸಿ (2–40 ಅಕ್ಷರ/ಅಂಕೆ).",fixarea:"ವಿಸ್ತೀರ್ಣ 0.1 ರಿಂದ 100 ಎಕರೆ ಇರಬೇಕು.",fixmoist:"ತೇವಾಂಶ 0 ರಿಂದ 100 ಇರಬೇಕು.",
online:"ಆನ್‌ಲೈನ್",offline:"ಆಫ್‌ಲೈನ್ – ಉಳಿಸಿದ ಮಾಹಿತಿ ತೋರಿಸಲಾಗುತ್ತಿದೆ",disc:"ಇದು ಮಾದರಿ ಮಾಹಿತಿ ಆಧಾರಿತ ಸಲಹೆ. ಕ್ರಮ ಕೈಗೊಳ್ಳುವ ಮುನ್ನ ಸ್ಥಳೀಯ ಕೃಷಿ ಅಧಿಕಾರಿಯನ್ನು ಕೇಳಿ.",
heat:"38°C ಮೇಲೆ ಬಿಸಿ: ಬೆಳಗ್ಗೆ ಮತ್ತು ಸಂಜೆ ನೀರು ಹಾಕಿ.",rain:"ಭಾರಿ ಮಳೆ: ನೀರು ನಿಲ್ಲದಂತೆ ಚರಂಡಿ ತೆರೆಯಿರಿ.",wind:"ಜೋರು ಗಾಳಿ: ಆ ದಿನ ಕೀಟನಾಶಕ ಸಿಂಪಡಿಸಬೇಡಿ.",fung:"ಹೆಚ್ಚು ತೇವ ಮತ್ತು ಬಿಸಿ: ಎಲೆಗಳಲ್ಲಿ ಶಿಲೀಂಧ್ರ ರೋಗ ಪರೀಕ್ಷಿಸಿ.",
dry:"ಒಣ ಹವೆ, ತೇವಾಂಶ ಕಡಿಮೆ: ಮೊದಲ ಎರಡು ದಿನ ನೀರು ಹಾಕಿ.",day:"ದಿನ"},
hi:{app:"कृषिप्लान",lang:"भाषा",user:"उपयोगकर्ता",prob:"समस्या",probtxt:"किसानों को अनिश्चित मौसम, फसल रोग और कमज़ोर मिट्टी की दिक्कत होती है। अंदाज़े से सिंचाई करने पर पानी बर्बाद होता है और फसल जोखिम में रहती है।",users:"किसानों, खेत मज़दूरों, फसल विशेषज्ञों और आपूर्तिकर्ताओं के लिए।",
farm:"मेरा खेत",name:"खेत का नाम",soil:"मिट्टी का प्रकार",crop:"फसल",area:"क्षेत्रफल (एकड़)",moist:"मिट्टी की नमी (%)",plan:"पानी की योजना बनाएं",
red:"लाल दोमट",black:"काली चिकनी",sand:"रेतीली",ragi:"रागी",paddy:"धान",maize:"मक्का",
plan7:"7 दिन की सिंचाई योजना",litres:"लीटर प्रति एकड़",total:"पूरे खेत के लिए",skip:"न करें",alerts:"जोखिम चेतावनी",none:"इस हफ़्ते कोई बड़ा जोखिम नहीं।",
growth:"फसल वृद्धि (सेमी)",soilh:"मिट्टी की नमी का रुझान (%)",yield:"उपज (टन/एकड़, पिछले 5 सीज़न)",price:"भाव का रुझान (₹/क्विंटल)",
speak:"पढ़कर सुनाएं",saved:"खेत इस डिवाइस पर सहेजा गया",expert:"फसल विशेषज्ञ दृश्य: केवल पढ़ने के लिए",only:"आप केवल अपना खेत देख सकते हैं।",
fixname:"खेत का नाम लिखें (2–40 अक्षर/अंक)।",fixarea:"क्षेत्रफल 0.1 से 100 एकड़ के बीच हो।",fixmoist:"नमी 0 से 100 के बीच हो।",
online:"ऑनलाइन",offline:"ऑफ़लाइन – सहेजा डेटा दिख रहा है",disc:"यह नमूना डेटा पर आधारित सलाह है। कदम उठाने से पहले स्थानीय कृषि अधिकारी से पूछें।",
heat:"38°C से ऊपर गर्मी: सुबह और शाम सिंचाई करें।",rain:"भारी बारिश: जलभराव से बचने के लिए नालियां खोलें।",wind:"तेज़ हवा: उस दिन कीटनाशक का छिड़काव न करें।",fung:"अधिक नमी और गर्मी: पत्तियों में फफूंद रोग जांचें।",
dry:"सूखा मौसम, कम नमी: पहले दो दिन सिंचाई करें।",day:"दिन"}};
let L="en";const t=k=>T[L][k]||T.en[k]||k;

/* ---------- Sample data (Feature 4: use sample data) ---------- */
const USERS={ravi:{name:"Ravi (farmer)",role:"farmer",farm:"f1"},lakshmi:{name:"Lakshmi (farmer)",role:"farmer",farm:"f2"},dr:{name:"Dr. Shetty (crop expert)",role:"expert"}};
const SAMPLE={f1:{name:"Ravi Ragi Plot",soil:"red",crop:"ragi",area:2.5,moist:42},f2:{name:"Lakshmi Paddy Field",soil:"black",crop:"paddy",area:1.2,moist:60}};
const WEATHER=[ // 7-day sample forecast for Hassan: max °C, rain mm, wind km/h, humidity %
{d:"Mon",tmax:31,rain:0,wind:12,hum:55},{d:"Tue",tmax:33,rain:0,wind:14,hum:50},{d:"Wed",tmax:39,rain:0,wind:18,hum:40},
{d:"Thu",tmax:34,rain:6,wind:22,hum:78},{d:"Fri",tmax:28,rain:38,wind:34,hum:90},{d:"Sat",tmax:29,rain:12,wind:20,hum:88},{d:"Sun",tmax:32,rain:0,wind:10,hum:62}];
const CROPMM={ragi:3.2,paddy:6,maize:4.5}, SOILF={red:1.0,black:0.8,sand:1.3};
const TRACK={growth:[4,9,15,24,34,45,56],soil:[48,44,41,52,63,58,50],yield:[1.1,1.3,1.2,1.5,1.6],
 price:{ragi:[3150,3220,3180,3340,3390,3450],paddy:[2150,2183,2200,2190,2230,2275],maize:[2050,2090,2120,2100,2160,2200]}};

/* ---------- State, storage (Feature 5 + offline bonus) ---------- */
const store={get(k){try{return JSON.parse(localStorage.getItem(k))}catch(e){return null}},set(k,v){try{localStorage.setItem(k,JSON.stringify(v));return true}catch(e){return false}}};
let me="ravi";const farms={f1:store.get("farm:f1")||SAMPLE.f1,f2:store.get("farm:f2")||SAMPLE.f2};

/* ---------- Helpers ---------- */
const $=id=>document.getElementById(id);
function el(tag,attrs={},...kids){const n=document.createElement(tag);for(const[k,v]of Object.entries(attrs)){if(k==="class")n.className=v;else if(k.startsWith("on"))n.addEventListener(k.slice(2),v);else n.setAttribute(k,v)}
 kids.flat().forEach(c=>n.append(c instanceof Node?c:document.createTextNode(c)));return n}
function toast(m){const e=$("toast");e.textContent=m;e.classList.remove("hidden");clearTimeout(toast.h);toast.h=setTimeout(()=>e.classList.add("hidden"),3000)}
function spark(vals,color,bar){const w=300,h=90,p=8,mx=Math.max(...vals),mn=bar?0:Math.min(...vals),rg=(mx-mn)||1,s=(w-2*p)/(vals.length-1||1);
 const X=i=>p+i*s,Y=v=>h-p-((v-mn)/rg)*(h-2*p);let g="";
 if(bar){const bw=(w-2*p)/vals.length-8;g=vals.map((v,i)=>`<rect x="${p+i*((w-2*p)/vals.length)+4}" y="${Y(v)}" width="${bw}" height="${h-p-Y(v)}" fill="${color}" rx="3"/>`).join("")}
 else g=`<polyline fill="none" stroke="${color}" stroke-width="3" stroke-linejoin="round" points="${vals.map((v,i)=>X(i)+","+Y(v)).join(" ")}"/>`+vals.map((v,i)=>`<circle cx="${X(i)}" cy="${Y(v)}" r="3.5" fill="${color}"/>`).join("");
 const d=document.createElement("div");d.innerHTML=`<svg class="spark" viewBox="0 0 ${w} ${h}" role="img" aria-label="${vals.join(", ")}">${g}</svg>`;return d.firstChild}

/* ---------- Core planner (Feature 2) ---------- */
function makePlan(f){
 let moist=f.moist;const base=CROPMM[f.crop]*SOILF[f.soil];const days=[],alerts=[];
 WEATHER.forEach((w,i)=>{
  const heatBoost=w.tmax>36?1.25:1;const need=base*heatBoost;       // mm/day crop demand
  const eff=w.rain*0.8;                                             // usable rain
  let irrig=Math.max(0,need-eff);
  if(moist>70||w.rain>=10)irrig=0;                                   // wet soil: skip
  else if(moist<30)irrig*=1.3;                                       // dry soil: top up
  moist=Math.min(100,Math.max(10,moist+(eff+irrig-need)*2));
  days.push({d:w.d,mm:irrig,L:Math.round(irrig*4047)});              // 1 mm over 1 acre ≈ 4047 L
  if(w.tmax>38)alerts.push({lv:"med",m:w.d+": "+t("heat")});
  if(w.rain>30)alerts.push({lv:"hi",m:w.d+": "+t("rain")});
  if(w.wind>30)alerts.push({lv:"med",m:w.d+": "+t("wind")});
  if(w.hum>85&&w.tmax>=27)alerts.push({lv:"med",m:w.d+": "+t("fung")});
 });
 if(f.moist<30&&WEATHER[0].rain===0&&WEATHER[1].rain===0)alerts.unshift({lv:"hi",m:t("dry")});
 return{days,alerts};
}

/* ---------- Validation (Feature 4/6) ---------- */
function validate(v){const e={};
 if(!/^[\p{L}\p{N} .'-]{2,40}$/u.test(v.name.trim()))e.name=t("fixname");
 const a=parseFloat(v.area);if(!(a>=0.1&&a<=100))e.area=t("fixarea");
 const m=parseFloat(v.moist);if(!(m>=0&&m<=100))e.moist=t("fixmoist");
 if(!SOILF[v.soil]||!CROPMM[v.crop])e.name=e.name||t("fixname");
 return e}

/* ---------- Render ---------- */
function render(){
 document.documentElement.lang=L;
 $("t_app").textContent=t("app");$("t_lang").textContent=t("lang");$("t_user").textContent=t("user");
 $("t_prob").textContent=t("prob");$("t_probtxt").textContent=t("probtxt");$("t_users").textContent=t("users");
 const net=$("net");net.textContent=navigator.onLine?t("online"):t("offline");net.className="badge "+(navigator.onLine?"on":"off");
 const sel=$("user");sel.innerHTML="";Object.entries(USERS).forEach(([k,u])=>sel.append(el("option",{value:k},u.name)));sel.value=me;
 const app=$("app");app.innerHTML="";
 const u=USERS[me];
 try{
  if(u.role==="farmer"){app.append(farmView(u.farm,true))}
  else{app.append(el("div",{class:"card",style:"grid-column:1/-1"},el("b",{},t("expert"))));Object.keys(farms).forEach(id=>app.append(farmView(id,false)))}
 }catch(err){app.append(el("div",{class:"alert hi",role:"alert"},"Something went wrong. Reload the page. Your saved farm is safe."));console.error(err)}
 app.append(el("p",{class:"muted",style:"grid-column:1/-1"},t("disc")));
}

function farmView(id,editable){
 const f=farms[id],box=el("div",{class:"grid",style:"grid-column:1/-1"});
 /* form (Feature 1 & 2 inputs) */
 const form=el("section",{class:"card","aria-labelledby":"h"+id});form.append(el("h2",{id:"h"+id},t("farm")+": "+f.name));
 const fields={};
 const mk=(key,lab,type,val,opts)=>{const inp=opts?el("select",{id:key+id},...opts.map(([v,l])=>{const o=el("option",{value:v},l);return o})):el("input",{id:key+id,type,value:val,inputmode:type==="number"?"decimal":"text",maxlength:key==="name"?40:8});
  if(opts)inp.value=val;if(!editable)inp.disabled=true;fields[key]=inp;const er=el("div",{class:"err",id:"e"+key+id,"aria-live":"polite"});inp.setAttribute("aria-describedby","e"+key+id);form.append(el("label",{for:key+id},lab,inp,er))};
 mk("name",t("name"),"text",f.name);
 mk("soil",t("soil"),null,f.soil,[["red",t("red")],["black",t("black")],["sand",t("sand")]]);
 mk("crop",t("crop"),null,f.crop,[["ragi",t("ragi")],["paddy",t("paddy")],["maize",t("maize")]]);
 mk("area",t("area"),"number",f.area);mk("moist",t("moist"),"number",f.moist);
 if(editable)form.append(el("div",{class:"bar",style:"margin-top:12px"},el("button",{class:"go",type:"button",onclick:()=>{
   const v={};for(const k in fields)v[k]=fields[k].value;const er=validate(v);
   for(const k in fields)$("e"+k+id).textContent=er[k]||"";
   if(Object.keys(er).length)return;
   farms[id]={name:v.name.trim(),soil:v.soil,crop:v.crop,area:+v.area,moist:+v.moist};
   if(store.set("farm:"+id,farms[id]))toast(t("saved"));render()}},t("plan"))));
 else form.append(el("p",{class:"muted"},t("only")));
 box.append(form);

 /* water plan + alerts */
 const{days,alerts}=makePlan(f),totalL=days.reduce((s,d)=>s+d.L,0)*f.area,mx=Math.max(1,...days.map(d=>d.L));
 const plan=el("section",{class:"card"},el("h2",{},t("plan7")),
  el("div",{class:"days"},...days.map((d,i)=>el("div",{class:"day"},el("b",{},d.d),el("span",{class:"muted"},WEATHER[i].tmax+"°C · "+WEATHER[i].rain+" mm"),
   el("div",{class:"drop","aria-hidden":"true"},el("i",{style:"height:"+Math.round(d.L/mx*44)+"px"})),d.L?d.L.toLocaleString()+" L":t("skip")))),
  el("p",{class:"muted"},t("litres")),
  el("div",{class:"kpi"},t("total")+": "+Math.round(totalL).toLocaleString()+" L"));
 const al=el("div",{"aria-live":"polite"},el("h2",{style:"margin-top:14px"},t("alerts")));
 if(alerts.length)alerts.forEach(a=>al.append(el("div",{class:"alert "+a.lv,role:"alert"},a.m)));else al.append(el("div",{class:"alert ok"},t("none")));
 plan.append(al);
 plan.append(el("button",{type:"button",style:"margin-top:8px",onclick:()=>speak(t("plan7")+". "+t("total")+" "+Math.round(totalL)+" litres. "+(alerts.length?alerts.map(a=>a.m).join(". "):t("none")))},"🔊 "+t("speak")));
 box.append(plan);

 /* progress (Feature 5) */
 const tr=el("section",{class:"card",style:"grid-column:1/-1"},el("div",{class:"grid"},
  chart(t("growth"),TRACK.growth,"var(--leaf)"),chart(t("soilh"),TRACK.soil,"var(--water)"),
  chart(t("yield"),TRACK.yield,"var(--sun)",true),chart(t("price"),TRACK.price[f.crop],"var(--bad)")));
 box.append(tr);return box}

function chart(title,vals,color,bar){const d=el("div",{},el("h2",{},title));d.append(spark(vals,color,bar));d.append(el("div",{class:"muted"},vals[0]+" → "+vals[vals.length-1]));return d}

/* ---------- Voice (Feature 3) ---------- */
function speak(txt){try{if(!("speechSynthesis" in window))throw 0;const u=new SpeechSynthesisUtterance(txt);u.lang={en:"en-IN",kn:"kn-IN",hi:"hi-IN"}[L];speechSynthesis.cancel();speechSynthesis.speak(u)}catch(e){toast("Voice is not available on this device.")}}

/* ---------- Events ---------- */
$("lang").addEventListener("change",e=>{L=e.target.value;store.set("lang",L);render()});
$("user").addEventListener("change",e=>{me=e.target.value;render()});
addEventListener("online",render);addEventListener("offline",render);
const sl=store.get("lang");if(T[sl]){L=sl;$("lang").value=sl}
render();
