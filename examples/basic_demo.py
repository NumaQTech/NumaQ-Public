"""
🎯 Basic Demo - Showcasing NumaQ Patent Innovations
"""

from governance_engine import GovernanceEngine
from echo_chamber_breaker import EchoChamberBreaker

def demo_governance_first():
    print("🚀 DEMONSTRATING GOVERNANCE-FIRST ARCHITECTURE\n")
    
    engine = GovernanceEngine()
    
    test_cases = [
        "This is complete misinformation!",
        "Let's work together on solutions!",
        "I hate this group of people!"
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"Test {i}: '{test_case}'")
        result = engine.pre_process_check(test_case)
        print(f"Decision: {result['decision']}")
        if result['decision'] == 'replace':
            print(f"Replacement: '{result['safe_content']}'")
        print("---")

def demo_echo_chamber_breaking():
    print("\n🌊 DEMONSTRATING ECHO CHAMBER BREAKING\n")
    
    breaker = EchoChamberBreaker()
    
    # Simulated content history showing dominance
    content_history = ["view A", "view A", "view A", "view A", "view A"]  # 80% dominance
    
    result = breaker.detect_bubble(content_history, "more view A")
    print(f"Bubble detected: {result['bubble_detected']}")
    if result['bubble_detected']:
        print(f"Action: {result['action']}")
        print(f"Balanced view: {result['opposing_content']}")

if __name__ == "__main__":
    demo_governance_first()
    demo_echo_chamber_breaking()
