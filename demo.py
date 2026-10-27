"""
Educational demonstration: fictional compound ranking.

This is NOT a trained AI model and does NOT use real drug data.
All values are invented solely to demonstrate a weighted-score workflow.
The scores do not indicate safety, efficacy, or suitability as medicines.
"""

compounds = [
    {"name": "Fictional Compound A", "feature_1": 0.80, "feature_2": 0.60},
    {"name": "Fictional Compound B", "feature_1": 0.55, "feature_2": 0.90},
    {"name": "Fictional Compound C", "feature_1": 0.70, "feature_2": 0.70},
]

# Arbitrary teaching weights, not scientifically validated.
weight_1 = 0.6
weight_2 = 0.4

for compound in compounds:
    compound["illustrative_score"] = (
        weight_1 * compound["feature_1"]
        + weight_2 * compound["feature_2"]
    )

ranked = sorted(
    compounds,
    key=lambda item: item["illustrative_score"],
    reverse=True,
)

print("FICTIONAL EDUCATIONAL EXAMPLE — NOT A DRUG PREDICTION")
print("-" * 55)

for rank, compound in enumerate(ranked, start=1):
    print(
        f"{rank}. {compound['name']}: "
        f"{compound['illustrative_score']:.2f}"
    )

print("\nReminder: these invented scores do not measure safety or effectiveness.")
