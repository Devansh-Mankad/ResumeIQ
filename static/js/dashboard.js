// Stop if no analysis has been performed yet
if (typeof chartData !== "undefined" && chartData && Object.keys(chartData).length > 0) {
    // ATS SCORE GAUGE
    Plotly.newPlot(
        "atsGauge",
        [
            {
                type: "indicator",
                mode: "gauge+number",
                value: chartData.ats,
                number: {suffix: "%"},
                title: {text: "Overall ATS Score"},
                gauge: {
                    axis: {
                        range: [0, 100]
                    },
                    bar: {
                        color: "#4F46E5"
                    },
                    steps: [
                        {
                            range: [0, 50],
                            color: "#FECACA"
                        },
                        {
                            range: [50, 75],
                            color: "#FDE68A"
                        },
                        {
                            range: [75, 100],
                            color: "#BBF7D0"
                        }
                    ]
                }
            }
        ],
        {
            margin: {
                t: 40,
                b: 20,
                l: 20,
                r: 20
            }
        },
        {
            responsive: true
        }
    );

    // SKILL MATCH PIE CHART
    Plotly.newPlot(
        "skillChart",
        [
            {
                values: [
                    chartData.matched,
                    chartData.missing
                ],
                labels: [
                    "Matched Skills",
                    "Missing Skills"
                ],
                type: "pie",
                hole: 0.55,
                textinfo: "label+percent",
                hoverinfo: "label+value+percent"
            }
        ],
        {
            margin: {
                t: 20,
                b: 20,
                l: 20,
                r: 20
            },
            showlegend: true
        },
        {
            responsive: true
        }
    );

    // ATS BREAKDOWN BAR CHART
    const breakdown = chartData.breakdown;
    Plotly.newPlot(
        "breakdownChart",
        [
            {
                x: [
                    breakdown.similarity,
                    breakdown.skills,
                    breakdown.projects,
                    breakdown.experience,
                    breakdown.education,
                    breakdown.certifications
                ],
                y: [
                    "Similarity",
                    "Skills",
                    "Projects",
                    "Experience",
                    "Education",
                    "Certificates"
                ],
                orientation: "h",
                type: "bar"
            }
        ],
        {
            margin: {
                l: 110,
                r: 20,
                t: 20,
                b: 40
            },
            xaxis: {
                title: "Score"
            }
        },
        {
            responsive: true
        }
    );
}

// ANALYSIS HISTORY CHART
if (typeof historyChart !== "undefined" && historyChart.length > 0) {
    Plotly.newPlot(
        "historyChart",
        [
            {
                x: historyChart.map(item => item.job),
                y: historyChart.map(item => item.score),
                mode: "lines+markers",
                type: "scatter",
                name: "ATS Score"
            }
        ],
        {
            xaxis: {
                title: "Job Role"
            },
            yaxis: {
                title: "ATS Score",
                range: [0, 100]
            },
            margin: {
                t: 20
            }
        },
        {
            responsive: true
        }
    );
}