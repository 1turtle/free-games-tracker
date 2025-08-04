import "./styles.css"
import { SiEpicgames } from "react-icons/si"
import { FaSteam } from "react-icons/fa"
import { FaPlaystation } from "react-icons/fa"
import { FaXbox } from "react-icons/fa"
import { SiGogdotcom } from "react-icons/si"


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
                            <div className="game">
                                <img className="game-img" alt="Hot air balloons" src="https://mdn.github.io/shared-assets/images/examples/balloons.jpg" />
                                <h3>Game Title</h3>
                            </div>

                            <div className="game">
                                <img className="game-img" alt="Hot air balloons" src="https://mdn.github.io/shared-assets/images/examples/balloons.jpg" />
                                <h3>Game Title</h3>
                            </div>
                            <div className="game">
                                <img className="game-img" alt="Hot air balloons" src="https://mdn.github.io/shared-assets/images/examples/balloons.jpg" />
                                <h3>Game Title</h3>
                            </div>
                            <div className="game">
                                <img className="game-img" alt="Hot air balloons" src="https://mdn.github.io/shared-assets/images/examples/balloons.jpg" />
                                <h3>Game Title</h3>
                            </div>
                        </div>
                    </div>

                    <div className="market">
                        <div className="market-name">
                            <FaSteam size="2rem" />
                            <h2>Steam</h2>
                        </div>

                        <div className="games">
                            <div className="game">
                                <img className="game-img" alt="Hot air balloons" src="https://mdn.github.io/shared-assets/images/examples/balloons.jpg" />
                                <h3>Game Title</h3>
                            </div>

                            <div className="game">
                                <img className="game-img" alt="Hot air balloons" src="https://mdn.github.io/shared-assets/images/examples/balloons.jpg" />
                                <h3>Game Title</h3>
                            </div>
                            <div className="game">
                                <img className="game-img" alt="Hot air balloons" src="https://mdn.github.io/shared-assets/images/examples/balloons.jpg" />
                                <h3>Game Title</h3>
                            </div>
                            <div className="game">
                                <img className="game-img" alt="Hot air balloons" src="https://mdn.github.io/shared-assets/images/examples/balloons.jpg" />
                                <h3>Game Title</h3>
                            </div>
                        </div>
                    </div>



                    <div className="market">
                        <div className="market-name">
                            <SiGogdotcom size="2rem" />
                            <h2>GoG Games</h2>
                        </div>

                        <div className="games">
                            <div className="game">
                                <img className="game-img" alt="Hot air balloons" src="https://mdn.github.io/shared-assets/images/examples/balloons.jpg" />
                                <h3>Game Title</h3>
                            </div>

                            <div className="game">
                                <img className="game-img" alt="Hot air balloons" src="https://mdn.github.io/shared-assets/images/examples/balloons.jpg" />
                                <h3>Game Title</h3>
                            </div>
                            <div className="game">
                                <img className="game-img" alt="Hot air balloons" src="https://mdn.github.io/shared-assets/images/examples/balloons.jpg" />
                                <h3>Game Title</h3>
                            </div>
                            <div className="game">
                                <img className="game-img" alt="Hot air balloons" src="https://mdn.github.io/shared-assets/images/examples/balloons.jpg" />
                                <h3>Game Title</h3>
                            </div>
                        </div>
                    </div>


                </div>
            </div>
        </>
    )
}
