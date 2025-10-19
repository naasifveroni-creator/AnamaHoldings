from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def landing_page():
    company_data = {
        'name': 'ANAMA HOLDINGS (PTY) LTD',
        'tagline': 'INDUSTRIAL WITH A BREAKER SPECTRUM',
        'reg_number': '2018/102808/07',
        'vat_number': '4880295441',
        'csd_number': 'MAAA0591007',
        
        'mission': 'To be the leaders in service delivery and quality in the construction, mining, infrastructure, energy and agriculture sectors throughout Africa whilst upholding our core values.',
        'vision': 'To become the customer\'s preferred choice, valuing quality, people and the environment.',
        
        'about': 'Since Anama Holdings establishment in 2018, the entity has been strategically expanding through multiple channels of valuable partnerships and technical expertise. It has since expanded its business sectors and geographical reach by realizing first and second tier opportunities, whilst developing its capacity and skills through multiple projects exposure.',
        
        'strategy': [
            'To be totally market driven',
            'To be internationally cost competitive',
            'To be South African market leader in all our product and service category',
            'To invest in the latest state of the art equipment',
            'To tie up with the right strategy alliance',
            'To comply with international environmental standards'
        ],
        
        'core_values': [
            {'title': 'SAFETY', 'description': 'At Anama Holdings we recognize the initial responsibility of operations as safety of all those involved. Following international standards: ISO 45001:2018, 9001, 14001 and OHSAS 18001.'},
            {'title': 'Integrity and accountability', 'description': 'In our practice we always believe in transparency, cascaded strategy and uncompromised development of management.'},
            {'title': 'Compassion', 'description': 'We live by the motto "caring is sharing", which directly translates to upliftment, employment training and experience through ongoing investment in people.'},
            {'title': 'Superior practice always', 'description': 'Our commitment to sound business processes paves the way to a superior product and service.'},
            {'title': 'Flexibility', 'description': 'Our hands-on and innovative management ensure a practical approach to service delivery whilst remaining flexible.'},
            {'title': 'Teamwork', 'description': 'We believe teams are an imperative component to the organisations success as they work towards a common goal.'}
        ],
        
        'services': [
            {
                'title': 'CIVIL CONSTRUCTION',
                'capabilities': [
                    'General civil and mining construction work',
                    'Concrete demolition, cutting and coring',
                    'Buildings and industrial civils',
                    'Water infrastructure repair',
                    'Bridge construction and repair',
                    'Road installation (pave, asphalt, concrete)',
                    'Storm water and drainage construction',
                    'Electrical sub-stations',
                    'Specialised flooring applications'
                ]
            },
            {
                'title': 'MINING',
                'capabilities': [
                    'Mine Site Construction / Capital Projects Support',
                    'Contract Mining (open pit design, load and haul, drill and blast)',
                    'Materials Handling (crushing, screening, stockpile management)',
                    'Rehabilitation and closure'
                ]
            },
            {
                'title': 'BULK EARTHWORKS AND ROADWORKS',
                'capabilities': [
                    'Clearing and earthworks',
                    'Township and mining infrastructure',
                    'Road construction and rehabilitation',
                    'Crushing and screening',
                    'Asphalt supply and surfacing',
                    'Landfill construction'
                ]
            },
            {
                'title': 'PLANT & EQUIPMENT HIRE',
                'capabilities': [
                    'Major earthworks equipment (ADTs, Dozers, Excavators)',
                    'Specialised equipment (Asphalt Pavers, Crushing Plants)',
                    'Major concrete equipment',
                    'Tools and equipment',
                    'Fuel storage solutions'
                ]
            }
        ],
        
        'client_industries': [
            'Mining',
            'Industrial construction', 
            'Power and energy',
            'Oil and gas',
            'Infrastructure',
            'Agriculture'
        ],
        
        'accreditations': [
            'B-BBEE LEVEL 1 CONTRIBUTOR: 135% PROCUREMENT RECOGNITION',
            'COIDA COMPLIANCE',
            'CIDB GRADING: CE - Civil Engineering, EP - Electrical Engineering Works, GB - General Building'
        ],
        
        'contact': {
            'address': '7631 Bellpepper Crescent, The Orchards 0182 South Africa',
            'phones': ['+27 84 298 4006', '+27 82 730 2546'],
            'emails': ['info@anama.co.za', 'tiyanih@anama.co.za'],
            'contacts': ['Mr. Tiyani Hongwane', 'Mr. Sello Motaung']
        }
    }
    return render_template('index.html', company=company_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
