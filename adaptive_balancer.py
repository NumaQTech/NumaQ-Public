"""
⚖️ NumaQ Adaptive Balancer - Patent Pending
Self-Regulating Discourse Health Management
"""

class AdaptiveBalancer:
    def __init__(self):
        self.over_dominance_threshold = 0.7
        self.under_representation_threshold = 0.2
        
    def calculate_balance_factor(self, current_score, context=None):
        """
        🔥 PATENTED MECHANISM:
        balanceFactor = (currentScore > 0.7) ? 0.6 : (currentScore < 0.2) ? 1.5 : 1.0
        """
        if current_score > self.over_dominance_threshold:
            return 0.6  # Reduziere Dominanz
        elif current_score < self.under_representation_threshold:
            return 1.5  # Fördern unterrepräsentierte Views
        else:
            return 1.0  # Neutral
        
    def assess_discourse_health(self, content_metrics):
        """Bewertet die Gesamtgesundheit des Diskurses"""
        health_score = self._calculate_health_score(content_metrics)
        
        return {
            "health_score": health_score,
            "status": self._get_health_status(health_score),
            "recommendations": self._generate_recommendations(content_metrics),
            "balance_factor": self.calculate_balance_factor(health_score),
            "patent_mechanism": "Adaptive Self-Balancing"
        }
    
    def _calculate_health_score(self, metrics):
        """Berechnet Diskurs-Gesundheits-Score"""
        # Vereinfachte Implementierung
        diversity_score = metrics.get("diversity", 0.5)
        toxicity_score = 1.0 - metrics.get("toxicity", 0.3)
        engagement_score = metrics.get("engagement", 0.6)
        
        return (diversity_score + toxicity_score + engagement_score) / 3
    
    def _get_health_status(self, score):
        if score > 0.7:
            return "healthy"
        elif score > 0.4:
            return "needs_attention"
        else:
            return "unhealthy"
    
    def _generate_recommendations(self, metrics):
        """Generiert Empfehlungen zur Verbesserung"""
        recommendations = []
        
        if metrics.get("diversity", 0) < 0.3:
            recommendations.append("Increase viewpoint diversity")
        if metrics.get("toxicity", 0) > 0.6:
            recommendations.append("Reduce toxic content")
            
        return recommendations
