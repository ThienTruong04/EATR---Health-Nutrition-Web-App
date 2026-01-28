// Chart.js visualizations for nutrition dashboard

let macrosChart = null;
let weeklyChart = null;

// Initialize macros pie chart
function updateMacrosChart(protein, carbs, fats) {
    const ctx = document.getElementById('macrosChart');
    if (!ctx) return;

    // Destroy existing chart if it exists
    if (macrosChart) {
        macrosChart.destroy();
    }

    macrosChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Protein', 'Carbs', 'Fats'],
            datasets: [{
                data: [protein, carbs, fats],
                backgroundColor: [
                    '#FF6384',
                    '#36A2EB',
                    '#FFCE56'
                ],
                borderWidth: 0
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function (context) {
                            return context.label + ': ' + Math.round(context.parsed) + 'g';
                        }
                    }
                }
            }
        }
    });
}

// Initialize weekly trend chart
function updateWeeklyChart(weekData) {
    const ctx = document.getElementById('weeklyChart');
    if (!ctx) return;

    // Destroy existing chart
    if (weeklyChart) {
        weeklyChart.destroy();
    }

    const labels = weekData.map(day => {
        const date = new Date(day.date);
        return date.toLocaleDateString('en-US', { weekday: 'short' });
    });

    const data = weekData.map(day => day.calories);

    weeklyChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Daily Calories',
                data: data,
                borderColor: '#10b981',
                backgroundColor: 'rgba(16, 185, 129, 0.1)',
                fill: true,
                tension: 0.4,
                pointRadius: 4,
                pointBackgroundColor: '#10b981'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function (context) {
                            return Math.round(context.parsed.y) + ' calories';
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    grid: {
                        color: 'rgba(0, 0, 0, 0.05)'
                    }
                },
                x: {
                    grid: {
                        display: false
                    }
                }
            }
        }
    });
}

// Add styles for nutrition dashboard
const nutritionStyles = `
    .nutrition-dashboard {
        padding: var(--spacing-lg) 0;
    }
    
    .goals-cards {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: var(--spacing-md);
        margin-bottom: var(--spacing-lg);
    }
    
    .goal-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: var(--spacing-md);
        border-radius: var(--radius-lg);
        text-align: center;
    }
    
    .goal-value {
        font-size: 2rem;
        font-weight: 700;
        margin: var(--spacing-sm) 0;
    }
    
    .dashboard-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: var(--spacing-lg);
        margin-bottom: var(--spacing-lg);
    }
    
    .dashboard-card {
        background: white;
        padding: var(--spacing-lg);
        border-radius: var(--radius-lg);
        box-shadow: var(--shadow-md);
    }
    
    .dashboard-card.full-width {
        grid-column: 1 / -1;
    }
    
    .dashboard-card h2 {
        margin-bottom: var(--spacing-md);
    }
    
    .progress-container {
        position: relative;
        text-align: center;
        margin-bottom: var(--spacing-md);
    }
    
    .progress-text {
        margin-top: var(--spacing-md);
    }
    
    .progress-text div {
        font-size: 2rem;
        font-weight: 700;
        color: var(--primary-color);
    }
    
    .progress-bar {
        height: 12px;
        background: var(--bg-secondary);
        border-radius: 10px;
        overflow: hidden;
    }
    
    .progress-fill {
        height: 100%;
        background: var(--gradient-primary);
        transition: width 0.5s ease;
    }
    
    .macros-legend {
        margin-top: var(--spacing-md);
    }
    
    .legend-item {
        display: flex;
        align-items: center;
        gap: var(--spacing-sm);
        margin-bottom: var(--spacing-sm);
    }
    
    .legend-color {
        width: 20px;
        height: 20px;
        border-radius: 4px;
    }
    
    .meals-log {
        background: white;
        padding: var(--spacing-lg);
        border-radius: var(--radius-lg);
        box-shadow: var(--shadow-md);
    }
    
    .meal-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: var(--spacing-sm);
        border-bottom: 1px solid var(--border-color);
    }
    
    .meal-type {
        display: inline-block;
        background: var(--bg-secondary);
        padding: 0.25rem 0.5rem;
        border-radius: var(--radius-sm);
        font-size: 0.75rem;
        margin-left: var(--spacing-sm);
    }
    
    .empty-state {
        text-align: center;
        color: var(--text-secondary);
        padding: var(--spacing-lg);
    }
`;

const styleSheet = document.createElement('style');
styleSheet.textContent = nutritionStyles;
document.head.appendChild(styleSheet);
