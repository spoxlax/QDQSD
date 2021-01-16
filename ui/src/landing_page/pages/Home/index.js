import React from 'react';
import loadable from '@loadable/component';

import Introduction from '../../content/introduction.json';
import FirstBlock from '../../content/firstBlock.json';
import SecondBlock from '../../content/secondBlock.json';
import ThirdBlock from '../../content/thirdBlock.json';
import FourthBlock from '../../content/fourthBlock.json';
import ContactBlock from '../../content/contactBlock.json';


const ContactFrom = loadable(() => import('../../components/ContactForm'));
const ContentBlock = loadable(() => import('../../components/ContentBlock'));
const MiddleBlock = loadable(() => import('../../components/MiddleBlock'));
const Container = loadable(() => import('../../common/Container'));
const ScrollToTop = loadable(() => import('../../common/ScrollToTop'));

const Home = () => {
    return (
        <Container>
            <ScrollToTop/>
            <ContentBlock
                comp={true}
                first="true"
                type="right"
                icon="developer.svg"
                title={Introduction.title}
                content={Introduction.text}
                button={Introduction.button}
            />
            <MiddleBlock
                title={FirstBlock.title}
                content={FirstBlock.text}
                button={FirstBlock.button}
            />
            <ContentBlock
                comp = {false}
                type="left"
                title={SecondBlock.title}
                content={SecondBlock.text}
                section={SecondBlock.section}
                icon="graphs.svg"
            />
            <ContentBlock
                comp = {false}
                type="right"
                title={ThirdBlock.title}
                content={ThirdBlock.text}
                icon="product-launch.svg"
            />

            <ContentBlock
                comp = {false}
                type="left"
                title={FourthBlock.title}
                content={FourthBlock.text}
                icon="waving.svg"
            />
            <ContactFrom title={ContactBlock.title} content={ContactBlock.text}/>
        </Container>
    );
};

export default Home;
