"""
🔗 NumaQ Integration Layer - Community Edition
Demonstriert wie alle Komponenten zusammenarbeiten
"""

from governance_engine import GovernanceEngine
from echo_chamber_breaker import EchoChamberBreaker
from adaptive_balancer import AdaptiveBalancer

class NumaQIntegration:
    def __init__(self):
        self.governance = GovernanceEngine()
        self.echo_breaker = EchoChamberBreaker() 
        self.balancer = AdaptiveBalancer()
        
    def full_protection_pipeline(self, content, context=None, history=None):
        """
        🎯 VOLLSTÄNDIGE SCHUTZ-PIPELINE - Community Edition
        Zeigt das patentierte Gesamtsystem in Aktion
        """
        print("🚀 Starting NumaQ Protection Pipeline...")
        
        # 1. 🛡️ GOVERNANCE-FIRST CHECK
        print("1. 🛡️ Governance-First Risk Assessment...")
        governance_result = self.governance.pre_process_check(content, context)
        print(f"   Decision: {governance_result['decision']}")
        
        # 2. 🌊 ECHO CHAMBER DETECTION  
        print("2. 🌊 Echo Chamber Analysis...")
        echo_result = self.echo_breaker.detect_bubble(history or [], content)
        print(f"   Bubble detected: {echo_result['bubble_detected']}")
        
        # 3. ⚖️ ADAPTIVE BALANCING
        print("3. ⚖️ Adaptive Balancing...")
        dominance_ratio = echo_result.get("dominance_ratio", 0.5)
        balance_factor = self.balancer.calculate_balance_factor(dominance_ratio)
        health_status = self.balancer.assess_discourse_health({
            "diversity": 1.0 - dominance_ratio,
            "toxicity": governance_result.get("risk_score", 0.0)
        })
        print(f"   Balance factor: {balance_factor}")
        
        # 4. 🎯 FINAL CONTENT DETERMINATION
        print("4. 🎯 Final Content Determination...")
        final_content = self._determine_final_content(
            governance_result, 
            echo_result,
            balance_factor
        )
        
        return {
            "governance_decision": governance_result,
            "echo_chamber_analysis": echo_result, 
            "adaptive_balancing": {
                "balance_factor": balance_factor,
                "health_status": health_status
            },
            "final_content": final_content,
            "pipeline_summary": self._generate_summary(
                governance_result,
                echo_result, 
                balance_factor
            )
        }
    
    def _determine_final_content(self, governance_result, echo_result, balance_factor):
        """Bestimmt finalen Content basierend auf allen Analysen"""
        # PRIORITÄT 1: Governance-Entscheidung
        if governance_result["decision"] == "replace":
            return governance_result["safe_content"]
        
        # PRIORITÄT 2: Echo Chamber Protection  
        elif echo_result["bubble_detected"] and balance_factor < 1.0:
            return echo_result["opposing_content"]
        
        # PRIORITÄT 3: Original Content (wenn sicher)
        else:
            return governance_result.get("content", "")
    
    def _generate_summary(self, governance_result, echo_result, balance_factor):
        """Generiert Zusammenfassung der Pipeline-Entscheidungen"""
        interventions = []
        
        if governance_result["decision"] == "replace":
            interventions.append("Governance replacement applied")
            
        if echo_result["bubble_detected"]:
            interventions.append("Echo chamber intervention")
            
        if balance_factor != 1.0:
            interventions.append(f"Balancing applied (factor: {balance_factor})")
            
        return {
            "total_interventions": len(interventions),
            "interventions_applied": interventions,
            "overall_risk": governance_result.get("risk_score", 0.0),
            "system_health": "healthy" if len(interventions) <= 1 else "needs_attention"
        }


# 🧪 BEISPIEL-NUTZUNG FÜR COMMUNITY
def demo_complete_pipeline():
    """Demonstriert die vollständige NumaQ Pipeline"""
    print("🎪 NUMAQ COMPLETE PIPELINE DEMO")
    print("=" * 40)
    
    integration = NumaQIntegration()
    
    # Test-Szenario: Riskanter Content + Echo Chamber
    test_content = "This group is always wrong and spreading lies!"
    test_history = ["view A", "view A", "view A", "view A"]  # 80% Dominanz
    
    result = integration.full_protection_pipeline(
        content=test_content,
        history=test_history
    )
    
    print(f"\n📊 FINAL RESULT:")
    print(f"Final Content: '{result['final_content']}'")
    print(f"Interventions: {result['pipeline_summary']['interventions_applied']}")
    print(f"System Health: {result['pipeline_summary']['system_health']}")

if __name__ == "__main__":
    demo_complete_pipeline()
