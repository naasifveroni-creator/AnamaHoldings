from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def landing_page():
    company_data = {
        'name': 'ANAMA HOLDINGS (PTY) LTD',
        'tagline': 'INNOVATION WITH A BROADER SPECTRUM',
        'reg_number': '2018/102808/07',
        'vat_number': '4880295441',
        'csd_number': 'MAAA0591007',
        
        'mission': 'To be the leaders in service delivery and quality in the construction, mining, infrastructure, energy and agriculture sectors throughout Africa whilst upholding our core values.',
        'vision': 'To become the customer\'s preferred choice, valuing quality, people and the environment.',
        
        'about': 'Since our establishment in 2018, ANAMA Holdings has been strategically expanding through valuable partnerships and technical expertise. We deliver turnkey solutions and support to South African based companies across multiple sectors.',
        
        'services': [
            {
                'title': 'Civil and Construction',
                'capabilities': [
                    'Buildings & Industrial Civils',
                    'Bridge Construction & Repair',
                    'Road Installation',
                    'Water Infrastructure',
                    'Electrical Sub-stations'
                ],
                'description': 'Full spectrum civil engineering services'
            },
            {
                'title': 'Mining Operations',
                'capabilities': [
                    'Contract Mining',
                    'Site Infrastructure',
                    'Materials Handling',
                    'Rehabilitation & Closure'
                ],
                'description': 'Africa-wide turnkey mining support'
            },
            {
                'title': 'Earthworks & Roadworks',
                'capabilities': [
                    'Earthworks & Clearing',
                    'Road Construction',
                    'Crushing & Screening',
                    'Township Infrastructure'
                ],
                'description': 'Complete bulk earthworks and roads contracts'
            },
            {
                'title': 'Plant & Equipment Hire',
                'capabilities': [
                    'Earthmoving Equipment',
                    'Specialized Machinery',
                    'Concrete Equipment',
                    'Tools & Support'
                ],
                'description': 'Premium equipment and support vehicles'
            },
            {
                'title': 'CIDB Grading',
                'capabilities': [
                    'CE - Civil Engineering',
                    'EP - Electrical Engineering Works — Infrastructure',
                    'GB - General Building',
                    'SH - Landscaping, irrigation and horticulture works',
                    'SO - Water supply and drainage for buildings (wet services, plu)'
                ],
                'description': 'Registered Construction Industry Capabilities'
            }
        ],
        
        'core_values': [
            {'title': 'Safety First', 'description': 'Highest priority on safety following international standards including ISO 45001, 9001, 14001 and OHSAS 18001'},
            {'title': 'Integrity', 'description': 'Transparency, accountability and uncompromised development in all our operations'},
            {'title': 'Compassion', 'description': 'Caring is sharing - upliftment, employment training and community investment'},
            {'title': 'Excellence', 'description': 'Superior practice always, delivering quality products and services'},
            {'title': 'Flexibility', 'description': 'Adaptable to ever-changing environmental and customer requirements'},
            {'title': 'Teamwork', 'description': 'Combining various skills and knowledge for successful project completion'}
        ],
        
        'accreditations': [
            'B-BBEE LEVEL 1 CONTRIBUTOR',
            'COIDA COMPLIANCE', 
            'CIDB GRADING: CE • EP • GB • SH • SO'
        ],
        
        'contact': {
            'address': '7631 Bellpepper Crescent, The Orchards 0182 South Africa',
            'phone': '070 717 3068',
            'emails': ['info@anama.co.za', 'tiyanih@anama.co.za'],
            'contacts': ['Mr. Tiyani Hongwane', 'Mr. Sello Motaung']
        }
    }
    return render_template('index.html', company=company_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
