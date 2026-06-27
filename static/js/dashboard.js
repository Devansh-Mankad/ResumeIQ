if (typeof chartData !== "undefined" && Object.keys(chartData).length > 0) {
    // ATS Gauge
    Plotly.newPlot(
        "atsGauge",
        [{
            type: "indicator",
            mode: "gauge+number",
            value: chartData.ats,
            number: {
                suffix: "%",
                font: {
                    size: 55
                }
            },
            title: {
                text: "<b>Overall ATS Score</b>",
                font: {
                    size: 20
                }
            },
            gauge: {
                shape: "angular",
                axis: {
                    range: [0,100],
                    tickwidth: 1,
                    tickcolor: "#6B7280"
                },
                bar: {
                    color: "#4F46E5",
                    thickness: 0.35
                },
                bgcolor: "white",
                borderwidth: 1,
                bordercolor: "#E5E7EB",
                steps: [
                    {
                        range:[0,50],
                        color:"#FECACA"
                    },
                    {
                        range:[50,75],
                        color:"#FDE68A"
                    },
                    {
                        range:[75,100],
                        color:"#BBF7D0"
                    }
                ]
            }
        }],
        {
            autosize:true,
            height:320,
            margin:{
                l:25,
                r:25,
                t:70,
                b:20
            },
            paper_bgcolor:"#FFFFFF",
            plot_bgcolor:"#FFFFFF"
        },
        {
            responsive:true,
            displayModeBar:false
        }
    );
    
    // Skill Match
    Plotly.newPlot(
        "skillChart",
        [{
            values:[
                chartData.matched,
                chartData.missing
            ],
            labels:[
                "Matched Skills",
                "Missing Skills"
            ],
            type:"pie",
            hole:0.60,
            textinfo:"label+percent",
            hoverinfo:"label+value",
            sort:false
        }],
        {
            autosize:true,
            height:320,
            margin:{
                l:10,
                r:10,
                t:20,
                b:20
            },
            showlegend:false,
            paper_bgcolor:"#FFFFFF",
            plot_bgcolor:"#FFFFFF"
        },
        {
            responsive:true,
            displayModeBar:false
        }
    );

    // ATS Breakdown
    const b = chartData.breakdown;
    Plotly.newPlot(
        "breakdownChart",
        [{
            x:[
                b.similarity,
                b.skills,
                b.projects,
                b.experience,
                b.education,
                b.certifications
            ],
            y:[
                "Similarity",
                "Skills",
                "Projects",
                "Experience",
                "Education",
                "Certificates"
            ],
            orientation:"h",
            type:"bar",
            marker:{
                color:"#4F46E5"
            }
        }],
        {
            autosize:true,
            height:320,
            margin:{
                l:120,
                r:20,
                t:20,
                b:40
            },
            xaxis:{
                range:[0,40],
                title:"Marks"
            },
            paper_bgcolor:"#FFFFFF",
            plot_bgcolor:"#FFFFFF"
        },
        {
            responsive:true,
            displayModeBar:false
        }
    );
}

// History Chart
if (typeof historyChart !== "undefined" && historyChart.length > 0){
    Plotly.newPlot(
        "historyChart",
        [{
            x:historyChart.map(i=>i.job),
            y:historyChart.map(i=>i.score),
            mode:"lines+markers",
            type:"scatter",
            line:{
                color:"#4F46E5",
                width:3
            },
            marker:{
                size:8
            }
        }],
        {
            autosize:true,
            height:320,
            margin:{
                l:50,
                r:20,
                t:20,
                b:70
            },
            yaxis:{
                range:[0,100],
                title:"ATS Score"
            },
            xaxis:{
                title:"Job Role"
            },
            paper_bgcolor:"#FFFFFF",
            plot_bgcolor:"#FFFFFF"
        },
        {
            responsive:true,
            displayModeBar:false
        }
    );
}

// Resize Charts
window.addEventListener("resize",function(){
    ["atsGauge","skillChart","breakdownChart","historyChart"].forEach(function(id){
        const chart=document.getElementById(id);
        if(chart){
            Plotly.Plots.resize(chart);
        }
    });

});