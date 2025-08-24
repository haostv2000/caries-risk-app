import streamlit as st

st.set_page_config(page_title="Оценка риска кариеса", page_icon="🦷")

st.title("🦷 Онлайн-тест: Определение риска кариеса")

st.write("Пожалуйста, выберите возрастную группу:")

age_group = st.radio("Возраст:", ["0–5 лет", "6+ лет"])

# ---------------- Функция оценки риска ----------------
def assess_risk_below_6(answers, protective, disease_indicators):
    high_risk = any([answers[0], answers[1], answers[2], answers[3], answers[6], answers[7]]) or any(disease_indicators)
    moderate_risk = any([answers[4],answers[5]]) and not high_risk
    if any(disease_indicators) or high_risk:
        return "Высокий"
    elif moderate_risk:
        return "Средний"
    else:
        return "Низкий"

def assess_risk_under_6(answers, protective, disease_indicators):
    high_risk = any([answers[0], answers[1], answers[5], answers[6], answers[7]]) or any(disease_indicators)
    moderate_risk = any([answers[2], answers[3], answers[4],answers[8],answers[9]]) and not high_risk
    if any(disease_indicators) or high_risk:
        return "Высокий"
    elif moderate_risk:
        return "Средний"
    else:
        return "Низкий"


# ---------------- Анкета для 0–5 лет ----------------
if age_group == "0–5 лет":
    st.header("Анкета для детей 0–5 лет")

    st.subheader("Факторы риска (социальные/поведенческие/медицинские)")
    q1 = st.checkbox("У матери/опекуна есть активный кариес")
    q2 = st.checkbox("Семья испытывает финансовые трудности / низкая медицинская грамотность)")
    q3 = st.checkbox("Ребёнок часто (более 3 раз в день) употребляет сладкие перекусы и/или сладкие напитки")
    q4 = st.checkbox("Ребёнок использует бутылочку или поильник со сладкой жидкостью")
    q5 = st.checkbox("Ребёнок — недавний иммигрант")
    q6 = st.checkbox("У ребёнка есть особые медицинские потребности")

    st.subheader("Факторы риска (клинические)")
    q7 = st.checkbox("На зубах ребёнка виден налёт")
    q8 = st.checkbox("Есть дефекты эмали")

    st.subheader("Защитные факторы")
    p1 = st.checkbox("Ребёнок получает фторированную воду или добавки")
    p2 = st.checkbox("Зубы чистятся фторсодержащей пастой")
    p3 = st.checkbox("Стоматолог наносил фторпрепараты местно")
    p4 = st.checkbox("У ребенка есть ежедневный домашний уход за зубами и регулярные визиты к стоматологу")

    st.subheader("Индикаторы заболевания")
    d1 = st.checkbox("Есть начальные кариозные поражения (белые пятна) ")
    d2 = st.checkbox("Есть явные кариозные полости")
    d3 = st.checkbox("Недавно были удалены зубы или лечены из-за кариеса")

    if st.button("Рассчитать риск"):
        all_answers = [q1, q2, q3, q4, q5, q6, q7, q8, p1, p2, p3, p4, d1, d2, d3]

        if not any(all_answers):  # проверка, что ВСЕ чекбоксы = False
            st.warning("⚠ Пожалуйста, ответьте на вопросы.")
        else:

            result = assess_risk_below_6(
                [q1,q2,q3,q4,q5,q6,q7,q8],
                [p1,p2,p3,p4],
                [d1,d2,d3]
            )
            if result == "Низкий":
                st.success("🎉 Поздравляю, у Вас низкий уровень кариеса!")
            else:
                st.error(f"⚠ У Вас {result.lower()} уровень кариеса. "
                         "Обязательно сообщите об этом своему стоматологу — он знает, что с этим делать и предложит Вам индивидуальную программу профилактики.")

# ---------------- Анкета для 6+ лет ----------------
else:
    st.header("Анкета для пациентов 6+ лет")

    st.subheader("Факторы риска (социальные/поведенческие/медицинские)")
    q1 = st.checkbox("Семья испытывает финансовые трудности / низкая медицинская грамотность)")
    q2 = st.checkbox("Частое употребление сладостей или сладких напитков (>3 раз в день)")
    q3 = st.checkbox("Пациент — недавний иммигрант")
    q4 = st.checkbox("Принимает лекарства, вызывающие сухость во рту")
    q5 = st.checkbox("Есть особые медицинские потребности")

    st.subheader("Факторы риска (клинические)")
    q6 = st.checkbox("Низкий уровень слюноотделения")
    q7 = st.checkbox("На зубах виден налёт")
    q8 = st.checkbox("Есть дефекты эмали")
    q9 = st.checkbox("Пациент носит ортодонтический или иной аппарат")
    q10 = st.checkbox("Есть некачественные пломбы")

    st.subheader("Защитные факторы")
    p1 = st.checkbox("Пациент получает фторированную воду")
    p2 = st.checkbox("Зубы чистятся фторсодержащей пастой")
    p3 = st.checkbox("Стоматолог наносил фторпрепараты местно")
    p4 = st.checkbox("Есть постоянный стоматолог/регулярные визиты")

    st.subheader("Индикаторы заболевания")
    d1 = st.checkbox("Есть межзубные кариозные поражения")
    d2 = st.checkbox("Есть новые начальные (белые пятна) кариозные поражения")
    d3 = st.checkbox("Есть новые кариозные поражения, видимые на рентгене")
    d4 = st.checkbox("Недавно были поставлены пломбы")

    if st.button("Рассчитать риск"):
        all_answers = [q1, q2, q3, q4, q5, q6, q7, q8,q9,q10, p1, p2, p3, p4, d1, d2, d3,d4]

        if not any(all_answers):  # проверка, что ВСЕ чекбоксы = False
            st.warning("⚠ Пожалуйста, ответьте на вопросы.")
        else:
            result = assess_risk_under_6(
                [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10],
                [p1,p2,p3,p4],
                [d1,d2,d3,d4]
            )
            if result == "Низкий":
                st.success("🎉 Поздравляю, у Вас низкий уровень кариеса!")
            else:
                st.error(f"⚠ У Вас {result.lower()} уровень кариеса. "
                         "Обязательно сообщите об этом своему стоматологу — он знает, что с этим делать и предложит Вам индивидуальную программу профилактики.")
