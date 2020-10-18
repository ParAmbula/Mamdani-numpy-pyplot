from simpful import *

FS = FuzzySystem()

TLV = AutoTriangle(3, terms=['poor', 'average', 'good'], universe_of_discourse=[-1,1])
FS.add_linguistic_variable("service", TLV)
FS.add_linguistic_variable("quality", TLV)

O1 = TriangleFuzzySet(-1,-1,-1,   term="low")
O2 = TriangleFuzzySet(0,0,0,  term="medium")
O3 = TriangleFuzzySet(1,1,1, term="high")
FS.add_linguistic_variable("tip", LinguisticVariable([O1, O2, O3], universe_of_discourse=[-1,1]))

FS.add_rules([
	"IF (quality IS poor) AND (service IS poor) THEN (tip IS low)",
    "IF (quality IS average) AND (service IS average) THEN (tip IS medium)",
    "IF (quality IS good) AND (service IS good) THEN (tip IS high)",
    "IF (quality IS poor) AND (service IS average) THEN (tip IS low)",
    "IF (quality IS poor) AND (service IS good) THEN (tip IS low)",
    "IF (quality IS average) AND (service IS poor) THEN (tip IS medium)",
    "IF (quality IS average) AND (service IS good) THEN (tip IS medium)",
    "IF (quality IS good) AND (service IS poor) THEN (tip IS medium)",
    "IF (quality IS good) AND (service IS average) THEN (tip IS high)",
	])

FS.set_variable("quality", 0.3)
FS.set_variable("service", -0.2)

tip = FS.inference()
print(tip)