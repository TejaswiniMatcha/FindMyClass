import blockA from '../assets/images/blockA.jpeg';
import blockB from '../assets/images/blockB.jpeg';
import blockC from '../assets/images/blockC.jpeg';
import blockD from '../assets/images/blockD.jpeg';
import centralBlock from '../assets/images/Centralblock.jpeg';
import freshmanBlock from '../assets/images/Freshmanblock.jpeg';
import oat from '../assets/images/OAT.jpeg';
import siemensBlock from '../assets/images/Siemensblock.jpeg';

export const blocks = [
  {
    slug: 'a-block',
    name: 'A Block',
    shortName: 'A',
    floors: 4,
    rooms: 24,
    description: 'Main academic block with lecture halls and faculty offices.',
    highlights: ['Smart classrooms', 'Seminar rooms', 'Faculty cabins'],
    icon: 'A',
    image: blockA,
  },
  {
    slug: 'b-block',
    name: 'B Block',
    shortName: 'B',
    floors: 4,
    rooms: 24,
    description: 'Engineering departments and lab spaces for core subjects.',
    highlights: ['Dept. of CSE', 'Project labs', 'Discussion rooms'],
    icon: 'B',
    image: blockB,
  },
  {
    slug: 'c-block',
    name: 'C Block',
    shortName: 'C',
    floors: 4,
    rooms: 24,
    description: 'Administrative offices and student services area.',
    highlights: ['Admissions desk', 'Examination cell', 'Support hub'],
    icon: 'C',
    image: blockC,
  },
  {
    slug: 'd-block',
    name: 'D Block',
    shortName: 'D',
    floors: 4,
    rooms: 24,
    description: 'Research and innovation block hosting workshops and studios.',
    highlights: ['Innovation labs', 'Design studio', 'Makerspace'],
    icon: 'D',
    image: blockD,
  },
  {
    slug: 'siemens-block',
    name: 'Siemens Block',
    shortName: 'SB',
    floors: 4,
    rooms: 24,
    description: 'Industry-oriented labs and specialized technical training spaces.',
    highlights: ['Automation labs', 'Training rooms', 'Demo hall'],
    icon: 'SB',
    image: siemensBlock,
  },
  {
    slug: 'freshman-block',
    name: 'Freshman Block',
    shortName: 'FB',
    floors: 4,
    rooms: 24,
    description: 'Freshman classrooms and mentoring rooms for first-year students.',
    highlights: ['Foundation courses', 'Mentoring zones', 'Study commons'],
    icon: 'FB',
    image: freshmanBlock,
  },
  {
    slug: 'central-block',
    name: 'Central Block',
    shortName: 'CB',
    floors: 4,
    rooms: 0,
    description: 'Campus hub for student activities and shared facilities.',
    highlights: ['Student lounge', 'Events area', 'Cafeteria'],
    icon: 'CB',
    image: centralBlock,
  },
  {
    slug: 'oat',
    name: 'OAT',
    shortName: 'OAT',
    floors: 0,
    rooms: 0,
    description: 'Open air theatre for cultural and academic events.',
    highlights: ['Gatherings', 'Cultural events', 'Open air sessions'],
    icon: 'OAT',
    image: oat,
  },
];

