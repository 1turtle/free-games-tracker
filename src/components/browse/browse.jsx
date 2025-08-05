import "./styles.css"
import { SiEpicgames } from "react-icons/si"
import { FaSteam } from "react-icons/fa"
import { FaPlaystation } from "react-icons/fa"
import { FaXbox } from "react-icons/fa"
import { SiGogdotcom } from "react-icons/si"
import { SiPrime } from "react-icons/si";
//import testData from "../../resources/test_data.json"
//import emptyData from "../../resources/empty.json"
import data from "../../resources/data.json"



export default function Browse() {
    return (
        <>
            <div id="free-games-cnt">
                <div id="free-games">
                    <div className="market">
                        <div className="market-name">
                            <SiEpicgames size="2rem" />
                            <h2>Epic Games</h2>
                        </div>

                        <div className="games">
                            {data.filter(game => game.market === "epic_games").map((game, i) =>
                                <a key={i} href={game.link} target="_blank" rel="noopener noreferrer" className="game">
                                    <img className="game-img" alt="game--img" src={game.img} />
                                    <h3 className="game-title-text">{game.title}</h3>
                                </a>
                            )}
                        </div>
                    </div>

                    <div className="market">
                        <div className="market-name">
                            <FaSteam size="2rem" />
                            <h2>Steam</h2>
                        </div>

                        <div className="games">
                            {data.filter(game => game.market === "steam").map((game, i) =>
                                <a key={i} href={game.link} target="_blank" rel="noopener noreferrer" className="game">
                                    <img className="game-img" alt="game--img" src={game.img} />
                                    <h3 className="game-title-text">{game.title}</h3>
                                </a>
                            )}
                        </div>
                    </div>

                    <div className="market">
                        <div className="market-name">
                            <SiGogdotcom size="2rem" />
                            <h2>GOG Games</h2>
                        </div>

                        <div className="games">
                            {data.filter(game => game.market === "gog").map((game, i) =>
                                <a key={i} href={game.link} target="_blank" rel="noopener noreferrer" className="game">
                                    <img className="game-img" alt="game--img" src={game.img} />
                                    <h3 className="game-title-text">{game.title}</h3>
                                </a>
                            )}
                        </div>
                    </div>

                    <div className="market">
                        <div className="market-name">
                            <FaPlaystation size="2rem" />
                            <h2>Playstation</h2>
                        </div>

                        <div className="games">
                            {data.filter(game => game.market === "playstation").map((game, i) =>
                                <a key={i} href={game.link} target="_blank" rel="noopener noreferrer" className="game">
                                    <img className="game-img" alt="game--img" src={game.img} />
                                    <h3 className="game-title-text">{game.title}</h3>
                                </a>
                            )}
                        </div>
                    </div>

                    <div className="market">
                        <div className="market-name">
                            <SiPrime size="2rem" />
                            <h2>Amazon Prime</h2>
                        </div>

                        <div className="games">
                            {data.filter(game => game.market === "amazon").map((game, i) =>
                                <a key={i} href={game.link} target="_blank" rel="noopener noreferrer" className="game">
                                    <img className="game-img" alt="game--img" src={game.img} />
                                    <h3 className="game-title-text">{game.title}</h3>
                                </a>
                            )}
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}
