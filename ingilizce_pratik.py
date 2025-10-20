import tkinter as tk
import random
import datetime

# =======================================================
# VERİ TABANI
# =======================================================

ingilizce_veritabani = {
    "I look forward to hearing from you soon.": "Yakında sizden haber bekliyorum.",
    "Could you please elaborate on your last point?": "Son noktanızı biraz açabilir misiniz?",
    "It is essential to take responsibility for our actions.": "Eylemlerimiz için sorumluluk almak esastır.",
    "Despite the difficulties, we managed to achieve our goal.": "Zorluklara rağmen amacımıza ulaşmayı başardık.",
    "The project's success is highly dependent on teamwork.": "Projenin başarısı büyük ölçüde ekip çalışmasına bağlıdır.",
    "The manager emphasized the importance of meeting the deadline.": "Yönetici, son teslim tarihine uymanın önemini vurguladı.",
    "Furthermore, we need to consider the long-term impact of this decision.": "Ayrıca, bu kararın uzun vadeli etkisini de göz önünde bulundurmalıyız.",
    "It appears that the main obstacle is the lack of resources.": "Görünüşe göre ana engel, kaynak eksikliğidir.",
    "You are strongly advised to back up your data regularly.": "Verilerinizi düzenli olarak yedeklemeniz şiddetle tavsiye edilir.",
    "His refusal to cooperate complicated the entire negotiation process.": "İşbirliği yapmayı reddetmesi, tüm müzakere sürecini zorlaştırdı.",
    "We must prioritize sustainability over immediate profit.": "Acil kâr yerine sürdürülebilirliğe öncelik vermeliyiz.",
    "The findings clearly demonstrate the effectiveness of the new method.": "Bulgular, yeni yöntemin etkinliğini açıkça göstermektedir.",
    "I'm deeply concerned about the increasing levels of pollution.": "Artan kirlilik seviyeleri konusunda derin endişe duyuyorum.",
    "This software is compatible with most operating systems.": "Bu yazılım, çoğu işletim sistemiyle uyumludur.",
    "It is crucial to verify the source of the information before sharing it.": "Bilgiyi paylaşmadan önce kaynağını doğrulamak hayati önem taşır.",
    "The committee will evaluate the proposals based on several criteria.": "Komite, teklifleri çeşitli kriterlere göre değerlendirecektir.",
    "She possesses a profound understanding of quantum physics.": "O, kuantum fiziği konusunda derin bir anlayışa sahiptir.",
    "The company decided to outsource its manufacturing operations.": "Şirket, üretim operasyonlarını dış kaynak kullanmaya karar verdi.",
    "Their primary objective is to enhance customer satisfaction.": "Temel amaçları müşteri memnuniyetini artırmaktır.",
    "He struggled to comprehend the complex instructions.": "Karmaşık talimatları anlamakta zorlandı."
}

kelime_veritabani = {
    "dependent": "bağlı",
    "essential": "gerekli",
    "elaborate": "detaylandırmak",
    "achieve": "ulaşmak",
    "forward": "ileri",
    "responsibility": "sorumluluk",
    "despite": "rağmen",
    "emphasize": "vurgulamak",
    "furthermore": "ayrıca",
    "obstacle": "engel",
    "advise": "tavsiye etmek",
    "refusal": "reddetme",
    "cooperate": "işbirliği yapmak",
    "negotiation": "müzakere",
    "impact": "etki",
    "deadline": "son teslim tarihi",
    "prioritize": "öncelik vermek",
    "sustainability": "sürdürülebilirlik",
    "effectiveness": "etkinlik",
    "concern": "endişe",
    "compatible": "uyumlu",
    "verify": "doğrulamak",
    "evaluate": "değerlendirmek",
    "profound": "derin",
    "outsource": "dış kaynak kullanmak",
    "objective": "amaç",
    "enhance": "artırmak",
    "struggle": "zorlanmak",
    "comprehend": "anlamak"
}

# =======================================================
# DİL VE TEMA AYARLARI
# =======================================================

AKTIF_DIL = "TR"  # TR veya EN
AKTIF_TEMA = "light" # light veya dark

DIL_AYARLARI = {
    "TR": {
        "menu_title": "B2 İngilizce Pratik Aracı - Ana Menü",
        "question_type": "Ne Çalışmak İstersin?",
        "btn_cumle": "CÜMLE ÇALIŞMA",
        "btn_kelime": "KELİME ÇALIŞMA",
        "btn_settings": "AYARLAR",
        "settings_title": "Ayarlar",
        "theme_label": "Uygulama Teması:",
        "lang_label": "Uygulama Dili:",
        "btn_save": "AYARLARI KAYDET",
        "theme_light": "Aydınlık Tema",
        "theme_dark": "Karanlık Tema",
        "lang_tr": "Türkçe",
        "lang_en": "İngilizce",
        "q_label": "Soru Sayısı Seçimi",
        "btn_menu": "Ana Menüye Dön",
        "q_intro": "için kaç soru istersin?",
        "q_btn_try_again": "Tekrar Dene",
        "q_btn_control": "Kontrol Et",
        "q_btn_new": "Yeni Soru",
        "q_label_intro": "Yukarıdaki İngilizce {0}ü çevirin.",
        "correct": "✓ Doğru!",
        "incorrect": "❌ Yanlış. Tekrar dene.",
        "placeholder": "Lütfen bir çeviri girin.",
        "quiz_title_c": "Cümle Çalışma",
        "quiz_title_w": "Kelime Çalışma",
        "quiz_complete": "Sınav Tamamlandı!",
        "score_total_q": "Toplam Soru:",
        "score_correct": "Doğru Cevap:",
        "score_wrong": "Yanlış Cevap:",
        "score_old": "Önceki Skor:",
        "score_improved": "Tebrikler! Önceki denemeden {0} fazla doğru yaptın. 🚀",
        "score_worse": "Biraz geriledin. {0} daha az doğru yaptın. 😥",
        "score_same": "Skorun önceki denemenle aynı.",
        "score_title_new": "Yeni Skorunuz:",
        "quiz_congrats": "TEBRİKLER! Bu moddaki tüm soruları bildin."
    },
    "EN": {
        "menu_title": "B2 English Practice Tool - Main Menu",
        "question_type": "What would you like to practice?",
        "btn_cumle": "SENTENCE PRACTICE",
        "btn_kelime": "WORD PRACTICE",
        "btn_settings": "SETTINGS",
        "settings_title": "Settings",
        "theme_label": "Application Theme:",
        "lang_label": "Application Language:",
        "btn_save": "SAVE SETTINGS",
        "theme_light": "Light Theme",
        "theme_dark": "Dark Theme",
        "lang_tr": "Turkish",
        "lang_en": "English",
        "q_label": "Question Count Selection",
        "btn_menu": "Return to Main Menu",
        "q_intro": "How many questions do you want?",
        "q_btn_try_again": "Try Again",
        "q_btn_control": "Check Translation",
        "q_btn_new": "New Question",
        "q_label_intro": "Translate the English {0} above.",
        "correct": "✓ Correct!",
        "incorrect": "❌ Wrong. Try again.",
        "placeholder": "Please enter a translation.",
        "quiz_title_c": "Sentence Practice",
        "quiz_title_w": "Word Practice",
        "quiz_complete": "Quiz Completed!",
        "score_total_q": "Total Questions:",
        "score_correct": "Correct Answers:",
        "score_wrong": "Wrong Answers:",
        "score_old": "Previous Score:",
        "score_improved": "Congrats! You got {0} more correct than last time. 🚀",
        "score_worse": "Slight setback. You got {0} less correct. 😥",
        "score_same": "Your score is the same as the previous attempt.",
        "score_title_new": "Your New Score:",
        "quiz_congrats": "CONGRATS! You correctly answered all questions in this mode."
    }
}


# =======================================================
# GLOBAL DEĞİŞKENLER
# =======================================================

mevcut_eng = "" 
mevcut_tr = ""
mevcut_mod = "" 

# Doğru Bilinenleri Tutacak Listeler
dogru_bilinen_cumleler = []
dogru_bilinen_kelimeler = []

# Skor Takibi
skor_dogru = 0
skor_yanlis = 0
skor_etiketleri = {} 
SECILEN_SORU_SAYISI = 0 
SORULACAK_LISTE = [] 
ONCEKI_SKORLAR = {} 

# =======================================================
# YARDIMCI FONKSİYONLAR
# =======================================================

def ekran_temizle():
    """Ana penceredeki tüm arayüz bileşenlerini temizler."""
    for widget in pencere.winfo_children():
        widget.destroy()

def uygulama_temasını_uygula():
    """Tüm pencereye ve bileşenlere aktif temayı uygular."""
    
    if AKTIF_TEMA == "dark":
        bg_color = "#333333" 
        fg_color = "white"   
        btn_bg = "#555555"
        btn_active_bg = "#777777"
        entry_bg = "#444444"
    else:
        bg_color = "SystemButtonFace" 
        fg_color = "black"
        btn_bg = "SystemButtonFace"
        btn_active_bg = "lightgray"
        entry_bg = "white"

    # Pencere arka planı
    pencere.config(bg=bg_color)
    
    # Tüm bileşenleri döngü ile güncelle
    for widget in pencere.winfo_children():
        try:
            # Temel arka plan ve yazı rengi
            widget.config(bg=bg_color, fg=fg_color)
            
            if isinstance(widget, tk.Button):
                 # Butonlar için özel renkler
                 widget.config(bg=btn_bg, fg=fg_color, activebackground=btn_active_bg, activeforeground=fg_color)
            if isinstance(widget, tk.Radiobutton):
                 # Radio butonlar için
                 widget.config(selectcolor=entry_bg)
            if isinstance(widget, tk.Entry):
                 # Giriş alanları için
                 widget.config(bg=entry_bg, fg=fg_color)
            if isinstance(widget, tk.Frame):
                # Frame'ler için
                widget.config(bg=bg_color)
                
        except Exception:
            pass
            
    # Eğer skor etiketleri varsa, arka planlarını güncelle
    if 'dogru' in skor_etiketleri:
        for etiket in skor_etiketleri.values():
            etiket.config(bg=bg_color)


def kontrol_et(cevirim_giris, sonuc_etiketi, ingilizce_ekran):
    """Kullanıcının çevirisini değerlendirir, skoru artırır ve bitişi kontrol eder."""
    global mevcut_tr, mevcut_eng, skor_dogru, skor_yanlis
    
    kullanici_ceviri = cevirim_giris.get().strip().lower()
    dogru_ceviri = mevcut_tr.strip().lower()
    
    if not kullanici_ceviri:
        sonuc_etiketi.config(text=DIL_AYARLARI[AKTIF_DIL]["placeholder"], fg="orange")
        return

    zaten_bilindi = mevcut_eng in (dogru_bilinen_cumleler if mevcut_mod == 'cumle' else dogru_bilinen_kelimeler)


    if kullanici_ceviri == dogru_ceviri:
        # BAŞARI DURUMU
        if not zaten_bilindi:
            skor_dogru += 1
            if mevcut_mod == 'cumle':
                dogru_bilinen_cumleler.append(mevcut_eng)
            else:
                dogru_bilinen_kelimeler.append(mevcut_eng)
            
        sonuc_etiketi.config(text=DIL_AYARLARI[AKTIF_DIL]["correct"], fg="green")
        cevirim_giris.config(bg="#d1ffc9", state='readonly') 
        ingilizce_ekran.config(bg="#d1ffc9")
        
    else:
        # HATA DURUMU
        if not zaten_bilindi:
             skor_yanlis += 1 
             
        sonuc_etiketi.config(text=DIL_AYARLARI[AKTIF_DIL]["incorrect"], fg="red")
        cevirim_giris.config(bg="#ffc9c9")
        
    # Skor etiketlerini güncelle
    skor_etiketleri['dogru'].config(text=f"✓ {skor_dogru}")
    skor_etiketleri['yanlis'].config(text=f"❌ {skor_yanlis}")
    
    # BİTİŞ KONTROLÜ
    if (skor_dogru + skor_yanlis) >= SECILEN_SORU_SAYISI:
        sonuc_ekrani()


def yeni_goster(ingilizce_ekran, cevirim_giris, sonuc_etiketi):
    """Sorulacak listeden sıradaki soruyu seçer."""
    global mevcut_eng, mevcut_tr
    
    veri_kaynagi = ingilizce_veritabani if mevcut_mod == 'cumle' else kelime_veritabani
    
    if (skor_dogru + skor_yanlis) >= SECILEN_SORU_SAYISI:
        sonuc_ekrani()
        return

    # Soru listesinden henüz sorulmamış/bilinmemiş bir soru bul
    sorulacak_adaylar = []
    dogru_bilinenler = dogru_bilinen_cumleler if mevcut_mod == 'cumle' else dogru_bilinen_kelimeler
    
    for soru in SORULACAK_LISTE:
        if soru not in dogru_bilinenler:
            sorulacak_adaylar.append(soru)
            break 

    if not sorulacak_adaylar:
        sonuc_ekrani()
        return 
    
    mevcut_eng = sorulacak_adaylar[0]
    mevcut_tr = veri_kaynagi[mevcut_eng] 
    
    # Ekranları güncelle
    ingilizce_ekran.config(text=mevcut_eng) 
    cevirim_giris.delete(0, tk.END)
    
    # Tema ayarlarını uygularken beyaz yap
    if AKTIF_TEMA == "dark":
         cevirim_giris.config(bg="#444444", fg="white", state='normal')
    else:
         cevirim_giris.config(bg="white", fg="black", state='normal')

    sonuc_etiketi.config(text=DIL_AYARLARI[AKTIF_DIL]["q_label_intro"].format("cümle" if mevcut_mod == 'cumle' else "kelime"), fg="black")
    ingilizce_ekran.config(bg="#f0f0f0") 
    
    # Soru numarasını güncelle
    soru_numarasi = skor_dogru + skor_yanlis + 1
    skor_etiketleri['kalan'].config(text=f"Soru {soru_numarasi} / {SECILEN_SORU_SAYISI}")
    uygulama_temasını_uygula()


# =======================================================
# EKRAN OLUŞTURUCULAR
# =======================================================

def ayarlar_menusu():
    """Uygulama dili ve tema ayarlarını gösterir."""
    global AKTIF_DIL, AKTIF_TEMA
    
    ekran_temizle()
    pencere.title(DIL_AYARLARI[AKTIF_DIL]["settings_title"])
    pencere.geometry("400x350")
    uygulama_temasını_uygula() # Tema uygula
    
    secilen_tema = tk.StringVar(value=AKTIF_TEMA)
    secilen_dil = tk.StringVar(value=AKTIF_DIL)

    tk.Label(pencere, text=DIL_AYARLARI[AKTIF_DIL]["settings_title"], font=('Arial', 20, 'bold')).pack(pady=20)

    # Tema Ayarları
    tk.Label(pencere, text=DIL_AYARLARI[AKTIF_DIL]["theme_label"], font=('Arial', 14)).pack(pady=10)
    
    # Bu Radio butonların arkaplanını Frame olmadan düzenlemek zor, direkt pencereye koyalım
    tk.Radiobutton(pencere, text=DIL_AYARLARI[AKTIF_DIL]["theme_light"], variable=secilen_tema, value="light", font=('Arial', 12)).pack()
    tk.Radiobutton(pencere, text=DIL_AYARLARI[AKTIF_DIL]["theme_dark"], variable=secilen_tema, value="dark", font=('Arial', 12)).pack()

    # Dil Ayarları
    tk.Label(pencere, text=DIL_AYARLARI[AKTIF_DIL]["lang_label"], font=('Arial', 14)).pack(pady=10)
    
    tk.Radiobutton(pencere, text=DIL_AYARLARI[AKTIF_DIL]["lang_tr"], variable=secilen_dil, value="TR", font=('Arial', 12)).pack()
    tk.Radiobutton(pencere, text=DIL_AYARLARI[AKTIF_DIL]["lang_en"], variable=secilen_dil, value="EN", font=('Arial', 12)).pack()

    def ayarları_kaydet():
        global AKTIF_DIL, AKTIF_TEMA
        AKTIF_DIL = secilen_dil.get()
        AKTIF_TEMA = secilen_tema.get()
        
        # Tema ve dil ayarını yaptıktan sonra menüye dön ve temanın uygulanmasını sağla
        ana_menu() 
        uygulama_temasını_uygula()

    tk.Button(pencere, text=DIL_AYARLARI[AKTIF_DIL]["btn_save"], command=ayarları_kaydet, font=('Arial', 12, 'bold'), bg="#ffc9d1").pack(pady=20)
    
    # GERİ DÖN BUTONU EKLENDİ
    tk.Button(pencere, text=DIL_AYARLARI[AKTIF_DIL]["btn_menu"], command=ana_menu, font=('Arial', 10)).pack()
    uygulama_temasını_uygula() # Tema ayarlarını kaydetme butonu için tekrar uygula


def soru_sayisi_secim_ekrani(baslik, mod):
    """Kullanıcıdan kaç soruluk test yapmak istediğini sorar."""
    ekran_temizle()
    uygulama_temasını_uygula()
    pencere.title(DIL_AYARLARI[AKTIF_DIL]["q_label"])
    pencere.geometry("400x350")
    
    max_soru = len(ingilizce_veritabani) if mod == 'cumle' else len(kelime_veritabani)
    
    tk.Label(pencere, text=f"{baslik} {DIL_AYARLARI[AKTIF_DIL]['q_intro']}", font=('Arial', 16, 'bold')).pack(pady=20)
    
    secenekler = [5, 10, 15]
    if max_soru not in secenekler:
        secenekler.append(max_soru) 
        
    for sayi in secenekler:
        if sayi <= max_soru:
            tk.Button(pencere, text=f"{sayi} Soru", 
                      command=lambda s=sayi: calisma_ekrani_olustur(baslik, mod, s), 
                      font=('Arial', 14), padx=20, pady=5).pack(pady=5)

    tk.Button(pencere, text=DIL_AYARLARI[AKTIF_DIL]["btn_menu"], command=ana_menu, font=('Arial', 10)).pack(pady=20)
    uygulama_temasını_uygula()


def calisma_ekrani_olustur(baslik, mod, soru_sayisi):
    """Cümle ve Kelime çalışma ekranlarını oluşturur ve testi başlatır."""
    global mevcut_mod, skor_dogru, skor_yanlis, skor_etiketleri, SECILEN_SORU_SAYISI, SORULACAK_LISTE
    mevcut_mod = mod
    SECILEN_SORU_SAYISI = soru_sayisi
    
    skor_dogru = 0
    skor_yanlis = 0
    
    tum_adaylar = list(ingilizce_veritabani.keys()) if mod == 'cumle' else list(kelime_veritabani.keys())
    random.shuffle(tum_adaylar) 
    SORULACAK_LISTE = tum_adaylar[:soru_sayisi] 
    
    ekran_temizle()
    uygulama_temasını_uygula()
    pencere.title(f"{baslik} ({soru_sayisi} Soru)")
    pencere.geometry("600x350" if mod == 'cumle' else "500x300")
    
    # SKOR GÖSTERİM ALANI (Arayüz)
    skor_cercevesi = tk.Frame(pencere)
    skor_cercevesi.pack(fill=tk.X, pady=5)
    uygulama_temasını_uygula() # Frame'in temasını güncelle
    
    skor_etiketleri['dogru'] = tk.Label(skor_cercevesi, text="✓ 0", font=('Arial', 14, 'bold'), fg="green")
    skor_etiketleri['dogru'].pack(side=tk.RIGHT, padx=5)

    skor_etiketleri['yanlis'] = tk.Label(skor_cercevesi, text="❌ 0", font=('Arial', 14, 'bold'), fg="red")
    skor_etiketleri['yanlis'].pack(side=tk.RIGHT, padx=5)
    
    skor_etiketleri['kalan'] = tk.Label(skor_cercevesi, text=f"Soru 1 / {soru_sayisi}", font=('Arial', 10))
    skor_etiketleri['kalan'].pack(side=tk.LEFT, padx=5)
    
    uygulama_temasını_uygula() # Skor etiketleri eklendikten sonra temayı tekrar uygula
    
    # Geri kalan arayüz
    ingilizce_ekran = tk.Label(pencere, text="", 
                               font=('Arial', 14 if mod == 'cumle' else 24, 'bold'), 
                               wraplength=550, justify=tk.LEFT,
                               bg="#f0f0f0", height=4 if mod == 'cumle' else 2) 
    ingilizce_ekran.pack(pady=20, fill=tk.X)

    cevirim_giris = tk.Entry(pencere, font=('Arial', 12), width=70)
    cevirim_giris.pack(pady=10)
    cevirim_giris.bind("<KeyRelease>", lambda event: cevirim_giris.config(bg="white", state='normal')) 

    sonuc_etiketi = tk.Label(pencere, text="...", font=('Arial', 10))
    sonuc_etiketi.pack(pady=5)
    
    # Buton Çerçevesi
    buton_cercevesi = tk.Frame(pencere)
    buton_cercevesi.pack(pady=20)
    
    tk.Button(buton_cercevesi, text=DIL_AYARLARI[AKTIF_DIL]["q_btn_control"], 
              command=lambda: kontrol_et(cevirim_giris, sonuc_etiketi, ingilizce_ekran), 
              font=('Arial', 12), padx=10, pady=5).pack(side=tk.LEFT, padx=10)

    tk.Button(buton_cercevesi, text=DIL_AYARLARI[AKTIF_DIL]["q_btn_new"], 
              command=lambda: yeni_goster(ingilizce_ekran, cevirim_giris, sonuc_etiketi), 
              font=('Arial', 12), padx=10, pady=5).pack(side=tk.LEFT, padx=10)
    
    tk.Button(pencere, text=DIL_AYARLARI[AKTIF_DIL]["btn_menu"], command=ana_menu, font=('Arial', 10)).pack(pady=5)
    
    yeni_goster(ingilizce_ekran, cevirim_giris, sonuc_etiketi)
    uygulama_temasını_uygula()


def sonuc_ekrani():
    """Tüm sorular bittiğinde sonucu gösterir, önceki skorla karşılaştırır ve yeniden deneme seçeneği sunar."""
    global mevcut_mod, skor_dogru, skor_yanlis, ONCEKI_SKORLAR
    
    ekran_temizle()
    uygulama_temasını_uygula()
    pencere.title(DIL_AYARLARI[AKTIF_DIL]["quiz_complete"])
    pencere.geometry("550x400")

    mod_baslik = DIL_AYARLARI[AKTIF_DIL]["quiz_title_c"] if mevcut_mod == 'cumle' else DIL_AYARLARI[AKTIF_DIL]["quiz_title_w"]
    toplam_soru = SECILEN_SORU_SAYISI
    
    tk.Label(pencere, text=f"{mod_baslik} {DIL_AYARLARI[AKTIF_DIL]['quiz_complete']}", font=('Arial', 20, 'bold')).pack(pady=20)
    
    # Skorları gösterme
    tk.Label(pencere, text=DIL_AYARLARI[AKTIF_DIL]["score_title_new"], font=('Arial', 14, 'underline')).pack()
    tk.Label(pencere, text=f"{DIL_AYARLARI[AKTIF_DIL]['score_correct']} {skor_dogru} | {DIL_AYARLARI[AKTIF_DIL]['score_wrong']} {skor_yanlis}", font=('Arial', 16, 'bold')).pack()
    
    # Önceki Skor Karşılaştırması
    if mevcut_mod in ONCEKI_SKORLAR:
        onceki_dogru = ONCEKI_SKORLAR[mevcut_mod]['doğru']
        onceki_yanlis = ONCEKI_SKORLAR[mevcut_mod]['yanlis']
        
        fark_dogru = skor_dogru - onceki_dogru
        
        if fark_dogru > 0:
            mesaj = DIL_AYARLARI[AKTIF_DIL]["score_improved"].format(fark_dogru)
            fg_color = "green"
        elif fark_dogru < 0:
            mesaj = DIL_AYARLARI[AKTIF_DIL]["score_worse"].format(abs(fark_dogru))
            fg_color = "red"
        else:
            mesaj = DIL_AYARLARI[AKTIF_DIL]["score_same"]
            fg_color = "blue"
            
        tk.Label(pencere, text=f"\n{DIL_AYARLARI[AKTIF_DIL]['score_old']} ({ONCEKI_SKORLAR[mevcut_mod]['tarih']}): {DIL_AYARLARI[AKTIF_DIL]['score_correct']} {onceki_dogru}, {DIL_AYARLARI[AKTIF_DIL]['score_wrong']} {onceki_yanlis}", font=('Arial', 10)).pack()
        tk.Label(pencere, text=mesaj, font=('Arial', 12, 'italic'), fg=fg_color).pack()
        
    # Mevcut skoru kaydet 
    ONCEKI_SKORLAR[mevcut_mod] = {'doğru': skor_dogru, 'yanlis': skor_yanlis, 'tarih': datetime.datetime.now().strftime("%H:%M")}
    
    # Tekrar Dene butonu
    tk.Button(pencere, text=DIL_AYARLARI[AKTIF_DIL]["q_btn_try_again"], 
              command=lambda: soru_sayisi_secim_ekrani(mod_baslik, mevcut_mod), 
              font=('Arial', 12), padx=20, pady=10).pack(pady=15)
    
    tk.Button(pencere, text=DIL_AYARLARI[AKTIF_DIL]["btn_menu"], command=ana_menu, font=('Arial', 10)).pack()
    uygulama_temasını_uygula()


def ana_menu():
    """Uygulama açılış menüsünü gösterir."""
    ekran_temizle()
    uygulama_temasını_uygula() 
    pencere.title(DIL_AYARLARI[AKTIF_DIL]["menu_title"])
    pencere.geometry("600x350")
    
    tk.Label(pencere, text=DIL_AYARLARI[AKTIF_DIL]["question_type"], font=('Arial', 20, 'bold')).pack(pady=30)
    
    btn_cumle = tk.Button(pencere, text=DIL_AYARLARI[AKTIF_DIL]["btn_cumle"], 
                          command=lambda: soru_sayisi_secim_ekrani(DIL_AYARLARI[AKTIF_DIL]["quiz_title_c"], 'cumle'), 
                          font=('Arial', 16), padx=30, pady=10, bg="#c9ffe0")
    btn_cumle.pack(pady=15)
    
    btn_kelime = tk.Button(pencere, text=DIL_AYARLARI[AKTIF_DIL]["btn_kelime"], 
                           command=lambda: soru_sayisi_secim_ekrani(DIL_AYARLARI[AKTIF_DIL]["quiz_title_w"], 'kelime'), 
                           font=('Arial', 16), padx=30, pady=10, bg="#c9e8ff")
    btn_kelime.pack(pady=15)
    
    # AYARLAR BUTONU DİĞERLERİYLE ORANTILI BÜYÜKLÜKTE
    btn_ayarlar = tk.Button(pencere, text=DIL_AYARLARI[AKTIF_DIL]["btn_settings"], 
                            command=ayarlar_menusu, 
                            font=('Arial', 14), padx=20, pady=8) # Boyut Ayarlandı
    btn_ayarlar.pack(pady=15)
    uygulama_temasını_uygula() 


# =======================================================
# UYGULAMA BAŞLANGICI
# =======================================================

pencere = tk.Tk()
pencere.config(padx=10, pady=10) 
ana_menu()
uygulama_temasını_uygula() # İlk başta da temayı uygula
pencere.mainloop()