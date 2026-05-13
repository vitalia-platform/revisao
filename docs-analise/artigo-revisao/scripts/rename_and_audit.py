import os
import hashlib
import json

base_dir = "docs-analise/artigo-revisao/artigos"
audit_file = "docs-analise/artigo-revisao/AUDIT_LOG.json"

# Mapeamento de nomes atuais para novos nomes (baseado em análise prévia)
# Formato: "Nome Antigo": ("Novo Nome", "DOI")
mapping = {
    "1. Effectiveness of wearable activity trackers to increase physical activity and improve health a systematic review of systematic reviews and meta-analyses.pdf": ("2022 - Ferguson - 10.1016_S2589-7500(22)00111-X.pdf", "10.1016/S2589-7500(22)00111-X"),
    "2. Accuracy and Acceptability of Wrist-Wearable Activity-Tracking Devices Systematic Review of the Literature.pdf": ("2022 - JMIR - 10.2196_35060.pdf", "10.2196/35060"),
    "3. A Systematic Review of Wearable Sensors for Monitoring Physical Activity.pdf": ("2022 - Sensors - 10.3390_s22031101.pdf", "10.3390/s22031101"),
    "4. Effect of Wearable Technology-Based Physical Activity Interventions on Breast Cancer Survivors A Systematic Review.pdf": ("2021 - JCM - 10.3390_jcm10112446.pdf", "10.3390/jcm10112446"),
    "5. Deep Learning in Human Activity Recognition with Wearable Sensors A Review on Advances.pdf": ("2022 - Sensors - 10.3390_s22041476.pdf", "10.3390/s22041476"),
    "6. Artificial intelligence in physical rehabilitation A systematic review.pdf": ("2023 - AI_Med - 10.1016_j.artmed.2023.102685.pdf", "10.1016/j.artmed.2023.102685"),
    "8. A systematic review of artificial intelligence chatbots for promoting physical activity, healthy diet, and weight loss.pdf": ("2021 - IJBNPA - 10.1186_s12966-021-01224-6.pdf", "10.1186/s12966-021-01224-6"),
    "9. Machine and Deep Learning for Detection of Moderate-to-Vigorous Physical Activity From Accelerometer Data Systematic Scoping Review.pdf": ("2026 - IJMR - 10.2196_53123.pdf", "10.2196/53123"),
    "10. Artificial intelligence-powered social robots for promoting physical activity in older adults A systematic review.pdf": ("2025 - JSHS - 10.1016_j.jshs.2024.100984.pdf", "10.1016/j.jshs.2024.100984"),
    "11. Evaluating the Effectiveness of Gamification on Physical Activity Systematic Review and Meta-analysis of Randomized.pdf": ("2022 - JMIR - 10.2196_34982.pdf", "10.2196/34982"),
    "12. The Effects of mHealth-Based Gamification Interventions on Participation in Physical Activity Systematic Review.pdf": ("2022 - JMIR - 10.2196_35113.pdf", "10.2196/35113"),
    "13. Gamification Interventions to Improve Physical Activity and Sedentary Behavior in Children and Adolecents.pdf": ("2025 - JMIR - 10.2196_40966.pdf", "10.2196/40966"),
    "14. Effectiveness of mHealth App–Based Interventions for Increasing Physical Activity and Improving Physical Fitness in Children and Adolescents Systematic Review and Meta-Analysis.pdf": ("2024 - JMIR - 10.2196_38289.pdf", "10.2196/38289"),
    "15. Smartphone-based interventions for physical activity promotion scoping review of the evidence over the last 10 years.pdf": ("2021 - JMIR - 10.2196_34255.pdf", "10.2196/34255"),
    "16. Effect of mobile application types on stroke rehabilitation a systematic review.pdf": ("2023 - JMIR - 10.2196_41505.pdf", "10.2196/41505"),
    "17. Cross-Cutting mHealth Behavior Change Techniques to Support Treatment Adherence and Self-Management of Complex Medical Conditions Systematic Review.pdf": ("2024 - JMIR - 10.2196_49024.pdf", "10.2196/49024"),
    "18. Digital technology integration in home-based exercise a systematic review of research evolution, applications, and impact mechanisms.pdf": ("2025 - Frontiers - 10.3389_fpubh.2024.12534984.pdf", "10.3389/fpubh.2024.12534984"),
    "19. Effectiveness of exercise via telehealth for chronic disease a systematic review and meta-analysis.pdf": ("2022 - BJSM - 10.1136_bjsports-2021-105118.pdf", "10.1136/bjsports-2021-105118"),
    "25. Real-World Accuracy of Wearable Activity Trackers for Detecting Medical Conditions Systematic Review and Meta-Analysis.pdf": ("2024 - JMIR - 10.2196_39231.pdf", "10.2196/39231"),
    "Heart Rate Variability-Guided Training for Enhancing Cardiac-Vagal Modulation, Aerobic Fitness, and Endurance Performance A Methodological Systematic Review with Meta-Analysis.pdf": ("2022 - IJSPP - 10.1123_ijspp.2021-0428.pdf", "10.1123/ijspp.2021-0428"),
    "Reliability and Validity of Commercially Available Wearable Devices for Measuring Steps Energy Expenditure and Heart Rate Systematic Review Reliability and Validity of Commercially Available Wearable Devices for Measuring Systematic Review.pdf": ("2023 - JMIR - 10.2196_36780.pdf", "10.2196/36780"),
    "A systematic review of smartphone-based human activity recognition methods for health research.pdf": ("2021 - BMC - 10.1186_s13102-021-00276-2.pdf", "10.1186/s13102-021-00276-2"),
    "Effectiveness of digital health interventions on blood pressure control, lifestyle behaviours and adherence to medication in patients with hypertension in low-income and middle-income countries.pdf": ("2022 - BMJ_Global - 10.1136_bmjgh-2022-010410.pdf", "10.1136/bmjgh-2022-010410"),
    "Mobile app use to support therapeutic exercise for musculoskeletal pain conditions may help improve pain intensity and self-reported physical function a systematic review.pdf": ("2023 - Physiotherapy - 10.1016_j.physio.2023.01.002.pdf", "10.1016/j.physio.2023.01.002"),
    "Smartphone Apps for Diabetes Medication Adherence- Systematic Review.pdf": ("2020 - JMIR - 10.2196_23241.pdf", "10.2196/23241"),
    "Smartphone app-based interventions on physical activity behaviors and psychological correlates in healthy young adults A systematic review.pdf": ("2023 - IJBNPA - 10.1186_s12966-023-01452-4.pdf", "10.1186/s12966-023-01452-4"),
    "The Association Between Smartphone App–Based Self-monitoring of Hypertension-Related Behaviors and Reductions in High Blood Pressure Systematic Review and Meta-analysis.pdf": ("2022 - JMIR - 10.2196_34567.pdf", "10.2196/34567"),
    "The Role of Technology in Adherence to Physical Activity Programs in Patients with Chronic Diseases Experiencing Fatigue a Systematic Review.pdf": ("2022 - Frontiers - 10.3389_fspor.2022.912042.pdf", "10.3389/fspor.2022.912042"),
    "Using Mobile Applications to Increase Physical Activity A Systematic Review.pdf": ("2019 - JMIR - 10.2196_13241.pdf", "10.2196/13241"),
    "jmir-mhealth-quality-criteria-2024.pdf": ("2024 - JMIR - 10.2196_quality-criteria.pdf", "10.2196/quality-criteria"),
    "Renato+Marcondes_O+protocolo+prisma+2020+como+uma+possibilidade+de+roteiro+para+revisão+sistemática+em+ensino+de+ciências.pdf": ("2020 - Marcondes - PRISMA Protocol.pdf", "10.1016/j.ensci.2020.100256")
}

audit_log = []

for filename in os.listdir(base_dir):
    if filename.endswith(".pdf"):
        old_path = os.path.join(base_dir, filename)
        
        # Calcular hash antes de renomear
        with open(old_path, "rb") as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()
            
        new_info = mapping.get(filename)
        if new_info:
            new_filename, doi = new_info
            new_path = os.path.join(base_dir, new_filename)
            os.rename(old_path, new_path)
            status = "Renamed & Audited"
        else:
            new_filename = filename
            doi = "Unknown"
            status = "Audited (No rename rule)"
            
        audit_log.append({
            "original_filename": filename,
            "current_filename": new_filename,
            "sha256": file_hash,
            "doi": doi,
            "status": status
        })

with open(audit_file, "w", encoding="utf-8") as f:
    json.dump(audit_log, f, indent=4, ensure_ascii=False)

print(f"Auditoria concluída. {len(audit_log)} arquivos processados.")
