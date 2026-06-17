/**
 * IIOS IGOS Scorecard Radar Chart Component
 * 
 * Visualizes the six core IIOS scores in an interactive radar chart.
 * Integrates with the IGOS Scorecard Template for real-time visualization.
 */

function initRadarChart(data) {
    const ctx = document.getElementById('radarChart').getContext('2d');
    
    new Chart(ctx, {
        type: 'radar',
        data: {
            labels: [
                'Cornerstone\n(20%)',
                'Integrity\n(20%)',
                'Compliance\n(20%)',
                'Risk\n(15%)',
                'Governance\n(15%)',
                'Development\n(10%)'
            ],
            datasets: [{
                label: 'Current Scores',
                data: [
                    data.cornerstone,
                    data.integrity,
                    data.compliance,
                    data.risk,
                    data.governance,
                    data.development
                ],
                backgroundColor: 'rgba(233, 69, 96, 0.2)',
                borderColor: '#e94560',
                borderWidth: 2,
                pointBackgroundColor: '#e94560',
                pointBorderColor: '#fff',
                pointHoverBackgroundColor: '#fff',
                pointHoverBorderColor: '#e94560'
            }, {
                label: 'Target (Platinum)',
                data: [95, 95, 95, 95, 95, 95],
                backgroundColor: 'rgba(107, 203, 119, 0.1)',
                borderColor: '#6bcb77',
                borderWidth: 2,
                borderDash: [5, 5],
                pointBackgroundColor: '#6bcb77',
                pointBorderColor: '#fff'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            scales: {
                r: {
                    beginAtZero: true,
                    max: 100,
                    min: 0,
                    ticks: {
                        stepSize: 20,
                        color: '#a0a0a0'
                    },
                    grid: {
                        color: 'rgba(233, 69, 96, 0.1)'
                    },
                    angleLines: {
                        color: 'rgba(233, 69, 96, 0.1)'
                    },
                    pointLabels: {
                        color: '#e94560',
                        font: {
                            size: 12,
                            weight: 'bold'
                        }
                    }
                }
            },
            plugins: {
                legend: {
                    labels: {
                        color: '#a0a0a0'
                    }
                },
                tooltip: {
                    backgroundColor: 'rgba(26, 26, 46, 0.9)',
                    titleColor: '#e94560',
                    bodyColor: '#fff',
                    borderColor: '#e94560',
                    borderWidth: 1
                }
            }
        }
    });
}

// Export for module usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { initRadarChart };
}